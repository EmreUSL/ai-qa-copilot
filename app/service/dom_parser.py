from bs4 import BeautifulSoup


class DomParser:
    def __init__(self, html_text: str):
        self.soup = BeautifulSoup(html_text, "lxml")

    def extract_elements(self):
        element = []
        tags_to_extract = ["input", "button", "select", "textarea", "a", "form"]

        for tag_name in tags_to_extract:
            found = self.soup.find_all(tag_name)

            for el in found:
                element.append({
                    "tag": tag_name,
                    "id": el.get("id"),
                    "name": el.get("name"),
                    "class": el.get("class"),
                    "placeholder": el.get("placeholder"),
                    "aria_label": el.get("aria-label"),
                    "text": el.get_text(strip=True)
                })

        return element