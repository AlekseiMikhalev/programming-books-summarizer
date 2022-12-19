from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.session import Base


class KnowledgeSection(Base):
    __tablename__ = 'knowledge_sections'

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='knowledge_sections')
    knowledge_concepts = relationship(
        'KnowledgeConcept', back_populates='knowledge_section')


class KnowledgeConcept(Base):
    __tablename__ = 'knowledge_concepts'

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, index=True)
    explanation = Column(String, index=True)
    knowledge_section_id = Column(Integer, ForeignKey('knowledge_sections.id'))

    knowledge_section = relationship(
        'KnowledgeSection', back_populates='knowledge_concepts')
    code_snippets = relationship(
        'CodeSnippet', back_populates='knowledge_concept')


class CodeSnippet(Base):
    __tablename__ = 'code_snippets'

    id = Column(Integer, primary_key=True)
    code = Column(String, index=True)
    description = Column(String, index=True)
    knowledge_concept_id = Column(Integer, ForeignKey('knowledge_concepts.id'))

    knowledge_concept = relationship(
        'KnowledgeConcept', back_populates='code_snippets')
