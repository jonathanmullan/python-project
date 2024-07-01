import time
import pytest

from playwright.sync_api import Playwright, sync_playwright


@pytest.fixture(scope="module")
def browser_context():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


def test_count_posts(browser_context):
    page = browser_context.new_page()
    page.goto("https://ocula.tech/resources")
    page.wait_for_load_state("networkidle")

    post_count = 0
    while True:
        print(f"Current URL: {page.url}")
        posts = page.locator('a.blog-more-link')
        number_of_posts = posts.count()
        print(f"Number of posts on this page: {number_of_posts}")
        post_count += number_of_posts

        older_posts_link = page.locator('a:has-text("Older Posts")')
        if older_posts_link.count() == 0:
            break

        older_posts_link.click()
        page.wait_for_load_state("networkidle")

    print(f"Total number of posts: {post_count}")


if __name__ == "__main__":
    pytest.main()
