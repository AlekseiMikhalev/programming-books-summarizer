from sqlalchemy.orm import Session
from sqlalchemy import and_
from fastapi import HTTPException, status

from users.models import User
from .models import KnowledgeSection, KnowledgeConcept, CodeSnippet
from .schemas import CodeSnippetCreate, KnowledgeSectionCreate, KnowledgeConceptCreate


class Library():

    def __init__(self, db: Session):
        self.db = db

    def get_section(self, user_id: int, skip: int = 0, limit: int = 100):
        sections = self.db.query(KnowledgeSection).filter(
            KnowledgeSection.user_id == user_id).offset(skip).limit(limit).all()
        return sections

    def create_section(self, section: str, user_id: int) -> KnowledgeSectionCreate:
        knowledge_section = self.db.query(KnowledgeSection).filter(
            KnowledgeSection.title == section).first()
        if knowledge_section is None:
            new_section = KnowledgeSection(
                title=section,
                user_id=user_id
            )
            self.db.add(new_section)
            self.db.commit()
            self.db.refresh(new_section)
            return new_section
        else:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail='Section already exists')

    def delete_section(self, section: str, user_id: int):
        knowledge_section = self.db.query(KnowledgeSection).filter(and_(
            KnowledgeSection.title == section,
            User.id == user_id)).first()
        if knowledge_section is not None:
            self.db.delete(knowledge_section)
            self.db.commit()
            return f'Knowledge section {section} was successfully deleted'
        return f'Knowledge sectoin {section} not found'

    def get_concept(self, skip: int = 0, limit: int = 100):
        return self.db.query(KnowledgeConcept).offset(skip).limit(limit).all()

    def create_concept(self, section: str, concept: str, explanation: str,
                       user_id: int) -> KnowledgeConceptCreate:
        knowledge_concept = self.db.query(KnowledgeConcept).filter(
            KnowledgeConcept.title == concept).first()
        knowledge_section = self.db.query(KnowledgeSection).filter(
            KnowledgeSection.title == section).first()
        if knowledge_section is None:
            new_section = KnowledgeSection(
                title=section,
                user_id=user_id
            )
            self.db.add(new_section)
            self.db.commit()
            self.db.refresh(new_section)
            knowledge_section = self.db.query(KnowledgeSection).filter(
                KnowledgeSection.title == section).first()
        if knowledge_concept is None:
            new_concept = KnowledgeConcept(
                knowledge_section_id=knowledge_section.id,
                title=concept,
                explanation=explanation
            )
            self.db.add(new_concept)
            self.db.commit()
            self.db.refresh(new_concept)
            return new_concept
        else:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail='Concept already exists')

    def delete_concept(self, concept: str, user_id: int):
        knowledge_concept = self.db.query(KnowledgeConcept).filter(and_(
            KnowledgeConcept.title == concept,
            User.id == user_id)).first()
        if knowledge_concept is not None:
            self.db.delete(knowledge_concept)
            self.db.commit()
            return f'Knowledge concept {concept} was successfully deleted'
        return f'Knowledge concept {concept} not found'

    def get_code_snippet(self, skip: int = 0, limit: int = 100):
        return self.db.query(CodeSnippet).offset(skip).limit(limit).all()

    def create_code_snippet(self, concept: str, code: str,
                            description: str) -> CodeSnippetCreate:
        knowledge_concept = self.db.query(KnowledgeConcept).filter(
            KnowledgeConcept.title == concept).first()
        if knowledge_concept is not None:
            new_code_snippet = CodeSnippet(
                knowledge_concept_id=knowledge_concept.id,
                code=code,
                description=description
            )
            self.db.add(new_code_snippet)
            self.db.commit()
            self.db.refresh(new_code_snippet)
            return new_code_snippet
        else:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="Couldn't find knowledge concept. Please create one first and try again.")


# def update_db_url_by_shorten_url(db: Session, shorten_url: str, new_shorten_url: str, user_id: int) -> URLs:
#     db_url = db.query(URLs).filter(URLs.shorten_url == shorten_url,
#                                    URLs.user_id == user_id).first()
#     if db_url is not None:
#         if db.query(URLs).filter(URLs.shorten_url == new_shorten_url).first():
#             return f'The shorten link {new_shorten_url} already exist'
#         else:
#             db_url.shorten_url = new_shorten_url
#             db.add(db_url)
#             db.commit()
#             db.refresh(db_url)
#             return db_url
#     return f'Short URL {shorten_url} not found'
