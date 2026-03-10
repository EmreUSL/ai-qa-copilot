from pydantic import BaseModel
from typing import Optional, List


class Element(BaseModel):

    tag: str

    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None

    class_name: Optional[List[str]] = None

    placeholder: Optional[str] = None
    aria_label: Optional[str] = None
    role: Optional[str] = None

    href: Optional[str] = None
    text: Optional[str] = None

    selector: Optional[str] = None

    score: Optional[int] = None