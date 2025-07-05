from fastapi import APIRouter, UploadFile, Request, Body, Form

from ai.ai_response import answer_to_photo, answer_to_text


router = APIRouter()


@router.post('/processing/photo/')
async def processing_photo(
    file: UploadFile = Form(),
    action: str = Form()
) -> str:
    image = await file.read()
    res = await answer_to_photo(image, action)
    
    return res

@router.post('/processing/text/')
async def processing_photo(
    text: str = Form(),
    action: str = Form()
) -> str:
    res = await answer_to_text(text, action)
    
    return res