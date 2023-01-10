from playwright.sync_api import sync_playwright
from parser import parse

# pip install pytest-playwright
# playwright install chromium


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://testing-www.codefellows.org")

        # click the Course Calendar link
        page.get_by_text("Course Calendar").click()

        page.click("//label[text()='400: Advanced']")

        # tracks are selected by default
        # so let's deselect all but the desired one

        courses = {
            "java": "Code 401: Java",
            "javascript": "Code 401: JavaScript",
            ".net": "Code 401: ASP.NET",
            "python": "Code 401: Python",
            "cybersecurity": "Ops 401: Cybersecurity",
        }

        course_key = "python"
        for course in courses:
            if course != course_key:
                page.click(f"//label[text() = '{courses[course]}']")

        markup = page.content()

        results = parse(markup)

        print(results)

        browser.close()


if __name__ == "__main__":
    main()
