from fastapi import APIRouter
from app.service.dom_parser import DomParser
from app.service.browser_renderer import BrowserRenderer

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/render-url")
async def render_url(url: str):

    renderer = BrowserRenderer()

    html_content = await renderer.render_url(url)

    parser = DomParser(html_content)
    elements = parser.extract_elements()

    return {
            "url": url,
            "element_count": len(elements),
            "elements_preview": elements[:10],
            "all_elements": elements
        }

