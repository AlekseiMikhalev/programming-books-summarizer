from fastapi import APIRouter

router = APIRouter()


@router.get('/summarizer/{portal_id}')
def access_portal(portal_id: int):
    return {'message': 'Programming Books Summarizer'}
