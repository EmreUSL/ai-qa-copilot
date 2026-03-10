from bs4 import BeautifulSoup

from app.model.element import Element


class DomParser:
    def __init__(self, html_text: str):
        self.soup = BeautifulSoup(html_text, "lxml")

    def extract_elements(self):

        elements = []

        tags_to_extract = [
            "input",
            "button",
            "select",
            "textarea",
            "a",
            "form"
        ]

        for tag_name in tags_to_extract:

            found = self.soup.find_all(tag_name)

            for el in found:

                text_value = el.get_text(strip=True)

                element_data = {
                    "tag": tag_name,
                    "id": el.get("id"),
                    "name": el.get("name"),
                    "type": el.get("type"),
                    "class_name": el.get("class"),
                    "placeholder": el.get("placeholder"),
                    "aria_label": el.get("aria-label"),
                    "role": el.get("role"),
                    "href": el.get("href"),
                    "data_testid": el.get("data-testid"),
                    "text": text_value,
                    "value": el.get("value"),
                    "selector": self._generate_selector(el)
                }

                if not self._is_meaningful(element_data):
                    continue

                element = Element(**element_data)
                elements.append(element.model_dump())

        return elements

    def _generate_selector(self, el):

        if el.get("id"):
            return f"#{el.get('id')}"

        if el.get("name"):
            return f"{el.name}[name='{el.get('name')}']"

        if el.get("class"):
            return f"{el.name}.{el.get('class')[0]}"

        return el.name

    def _is_meaningful(self, element):

        if element["text"]:
            return True

        if element["placeholder"]:
            return True

        if element["name"]:
            return True

        if element["aria_label"]:
            return True

        return False