import os
import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright
import json
import allure


@pytest.fixture(autouse=True)
def disable_pycache():
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

    
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def context(request, playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context

    results_dir = Path("test-results")
    results_dir.mkdir(exist_ok=True, parents=True)

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        trace_path = results_dir / f"{request.node.name}-trace.zip"
        context.tracing.stop(path=str(trace_path))
        print(f"Test failed: Trace saved to {trace_path}")
        allure.attach.file(str(trace_path), name="Trace", attachment_type=allure.attachment_type.TEXT)

        screenshot_path = results_dir / f"{request.node.name}-screenshot.png"
        page = context.pages[0]
        page.screenshot(path=str(screenshot_path))
        with open(screenshot_path, "rb") as image_file:
            allure.attach(image_file.read(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
    else:
        context.tracing.stop()

    context.close()
    browser.close()

@pytest.fixture
def credentials():
    with open('/c:/ArchiveAutomation/credentials.json') as f:
        return json.load(f)
