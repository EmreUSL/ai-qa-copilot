class ElementScorer:

    TAG_SCORES = {
        "input": 20,
        "button": 30,
        "form": 25,
        "select": 15,
        "textarea": 15,
        "a": 10
    }

    TYPE_SCORES = {
        "password": 40,
        "submit": 30,
        "email": 20,
        "search": 20
    }

    KEYWORD_SCORES = {
        "login": 40,
        "sign in": 40,
        "submit": 40,
        "search": 35,
        "checkout": 50,
        "buy": 50,
        "add to cart": 45,
        "register": 35,
        "signup": 35
    }

    NAME_SCORES = {
        "user": 35,
        "username": 35,
        "email": 35,
        "pass": 35,
        "password": 40
    }

    PLACEHOLDER_SCORES = {
        "search": 30,
        "email": 30,
        "username": 30
    }

    ARIA_SCORES = {
        "search": 35,
        "menu": 20,
        "login": 40
    }

    def __init__(self, elements):
        self.elements = elements

    def score_elements(self):

        scored_elements = []

        for el in self.elements:

            score = 0

            tag = el.get("tag")
            text = (el.get("text") or "").lower()
            placeholder = (el.get("placeholder") or "").lower()
            name = (el.get("name") or "").lower()
            element_type = (el.get("type") or "").lower()
            aria = (el.get("aria_label") or "").lower()

            # TAG SCORE
            score += self.TAG_SCORES.get(tag, 0)

            # TYPE SCORE
            score += self.TYPE_SCORES.get(element_type, 0)

            # TEXT KEYWORD SCORE
            for word, value in self.KEYWORD_SCORES.items():
                if word in text:
                    score += value

            # NAME SCORE
            for word, value in self.NAME_SCORES.items():
                if word in name:
                    score += value

            # PLACEHOLDER SCORE
            for word, value in self.PLACEHOLDER_SCORES.items():
                if word in placeholder:
                    score += value

            # ARIA SCORE
            for word, value in self.ARIA_SCORES.items():
                if word in aria:
                    score += value

            el["score"] = score

            scored_elements.append(el)

        return scored_elements

    def top_elements(self, limit=20):

        scored = self.score_elements()

        return sorted(
            scored,
            key=lambda x: x["score"],
            reverse=True
        )[:limit]