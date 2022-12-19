from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.session import get_db
from auth.service import get_current_user

from users.models import User
from library.schemas import (CodeSnippetCreate, KnowledgeSectionCreate,
                             KnowledgeConceptCreate, KnowledgeConceptRead,
                             KnowledgeSectionRead, CodeSnippetRead)
from library.service import Library


router = APIRouter(tags=['knowledge'])


def raise_bad_request(message):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail=message)


@router.get('/users/me/sections', response_model=list[KnowledgeSectionRead],
            status_code=status.HTTP_200_OK)
async def get_sections(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    knowledge_service = Library(db)
    return knowledge_service.get_section(current_user.id)


@router.post('/users/me/sections', response_model=KnowledgeSectionRead,
             status_code=status.HTTP_201_CREATED)
async def create_section(section: KnowledgeSectionCreate, db: Session = Depends(get_db),
                         current_user: User = Depends(get_current_user)):
    knowledge_service = Library(db)
    return knowledge_service.create_section(section.title, current_user.id)


@router.delete('/users/me/sections', status_code=status.HTTP_200_OK)
async def delete_section(section_title: str, db: Session = Depends(get_db),
                         current_user: User = Depends(get_current_user)):
    knowledge_service = Library(db)
    return knowledge_service.delete_section(section_title, current_user.id)


@router.get('/users/me/concepts', response_model=list[KnowledgeConceptRead],
            status_code=status.HTTP_200_OK)
async def get_concepts(db: Session = Depends(get_db),
                       current_user: User = Depends(get_current_user)):
    knowledge_service = Library(db)
    return knowledge_service.get_concept()


@router.post('/users/me/concepts', response_model=KnowledgeConceptRead,
             status_code=status.HTTP_201_CREATED)
async def create_concept(concept: KnowledgeConceptCreate, db: Session = Depends(get_db),
                         current_user: User = Depends(get_current_user)):
    knowledge_service = Library(db)
    return knowledge_service.create_concept(concept=concept.title, section=concept.knowledge_section,
                                            explanation=concept.explanation, user_id=current_user.id)


@router.delete('/users/me/concepts', status_code=status.HTTP_200_OK)
async def delete_concept(concept_title: str, db: Session = Depends(get_db),
                         current_user: User = Depends(get_current_user)):
    knowledge_service = Library(db)
    return knowledge_service.delete_concept(concept_title, current_user.id)


@router.get('/users/me/snippets', response_model=list[CodeSnippetRead],
            status_code=status.HTTP_200_OK)
async def get_snippets(db: Session = Depends(get_db),
                       current_user: User = Depends(get_current_user)):
    knowledge_service = Library(db)
    return knowledge_service.get_code_snippet()


@router.post('/users/me/snippets', response_model=CodeSnippetRead,
             status_code=status.HTTP_201_CREATED)
async def create_snippet(code_snippet: CodeSnippetCreate, db: Session = Depends(get_db),
                         current_user: User = Depends(get_current_user)):
    knowledge_service = Library(db)
    return knowledge_service.create_code_snippet(code=code_snippet.code,
                                                 description=code_snippet.description,
                                                 concept=code_snippet.knowledge_concept)


# @router.delete('/users/me/urls/delete', status_code=status.HTTP_200_OK)
# async def delete_url(shorten_url: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#     return delete_db_url_by_shorten_url(db=db, shorten_url=shorten_url, user_id=current_user.id)


# @router.put('/users/me/urls/update', status_code=status.HTTP_201_CREATED)
# async def update_url(shorten_url: str, new_shorten_url: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#     return update_db_url_by_shorten_url(db=db, shorten_url=shorten_url, new_shorten_url=new_shorten_url, user_id=current_user.id)
