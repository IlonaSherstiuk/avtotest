from playwright.sync_api import sync_playwright
from pytest import fixture


from models_staff.staff import Staff

@fixture
def get_test():
    with sync_playwright() as playwright:
        yield playwright


@fixture
def web_staff(get_test):
    staff = Staff(get_test)
    yield staff
    staff.close()
    if hasattr(staff, 'close'):
        staff.close()




