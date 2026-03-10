from fastapi import APIRouter
from app.service.dom_parser import DomParser
from app.service.browser_renderer import BrowserRenderer
from app.service.element_scoring import ElementScorer

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/render-url")
async def render_url(url: str):

    renderer = BrowserRenderer()

    html_content = await renderer.render_url(url)

    parser = DomParser(html_content)
    elements = parser.extract_elements()

    scorer = ElementScorer(elements)
    top_elements = scorer.top_elements()

    return {
        "url": url,
        "total_elements": len(elements),
        "important_elements": len(top_elements),
        "elements": top_elements
    }

