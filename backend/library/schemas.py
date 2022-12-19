from pydantic import BaseModel
from sqlalchemy import Integer


class CodeSnippet(BaseModel):
    code: str
    description: str


class CodeSnippetCreate(CodeSnippet):
    knowledge_concept: str

    class Config:
        orm_mode = True


class CodeSnippetRead(CodeSnippet):
    pass

    class Config:
        orm_mode = True


class KnowledgeConcept(BaseModel):
    title: str
    explanation: str

    class Config:
        orm_mode = True


class KnowledgeConceptCreate(KnowledgeConcept):
    knowledge_section: str
    code_snippets: list[CodeSnippetCreate] | None = None

    class Config:
        orm_mode = True


class KnowledgeConceptRead(KnowledgeConcept):
    code_snippets: list[CodeSnippetRead]

    class Config:
        orm_mode = True


class KnowledgeSection(BaseModel):
    title: str

    class Config:
        orm_mode = True


class KnowledgeSectionCreate(KnowledgeSection):
    knowledge_concepts: list[KnowledgeConceptCreate] | None = None

    class Config:
        orm_mode = True


class KnowledgeSectionRead(KnowledgeSectionCreate):
    knowledge_concepts: list[KnowledgeConceptRead]

    class Config:
        orm_mode = True
