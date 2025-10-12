"""Pydantic schemas for API request/response models."""

from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class ChamberEnum(str, Enum):
    """Congressional chamber."""

    SENATE = "senate"
    HOUSE = "house"


class PartyEnum(str, Enum):
    """Political party."""

    DEMOCRAT = "democrat"
    REPUBLICAN = "republican"
    INDEPENDENT = "independent"
    OTHER = "other"


class TransactionTypeEnum(str, Enum):
    """Transaction type."""

    BUY = "buy"
    SELL = "sell"
    EXCHANGE = "exchange"


class AssetTypeEnum(str, Enum):
    """Asset type."""

    STOCK = "stock"
    OPTION = "option"
    BOND = "bond"
    CRYPTO = "crypto"
    OTHER = "other"


class DocumentTypeEnum(str, Enum):
    """Document type."""

    SENATE_PTR = "senate_ptr"
    HOUSE_DISCLOSURE = "house_disclosure"
    SEC_FORM4 = "sec_form4"


# Base schemas
class PoliticianBase(BaseModel):
    """Base politician schema."""

    name: str = Field(..., description="Full name of the politician")
    chamber: ChamberEnum = Field(..., description="Congressional chamber")
    state: str = Field(..., max_length=2, description="Two-letter state code")
    party: PartyEnum = Field(..., description="Political party")
    in_office: bool = Field(default=True, description="Currently in office")
    photo_url: Optional[str] = Field(None, description="URL to photo")


class PoliticianCreate(PoliticianBase):
    """Schema for creating a politician."""

    pass


class Politician(PoliticianBase):
    """Full politician schema with ID."""

    id: UUID
    created_at: datetime

    model_config = {"from_attributes": True}


class AssetBase(BaseModel):
    """Base asset schema."""

    ticker: str = Field(..., max_length=10, description="Ticker symbol")
    name: str = Field(..., description="Full asset name")
    asset_type: AssetTypeEnum = Field(..., description="Asset type")


class AssetCreate(AssetBase):
    """Schema for creating an asset."""

    pass


class Asset(AssetBase):
    """Full asset schema with ID."""

    id: UUID

    model_config = {"from_attributes": True}


class TransactionBase(BaseModel):
    """Base transaction schema."""

    transaction_date: date = Field(..., description="Date of the transaction")
    transaction_type: TransactionTypeEnum = Field(..., description="Transaction type")
    ticker: str = Field(..., max_length=10, description="Ticker symbol")
    amount_min: Decimal = Field(..., description="Minimum transaction amount")
    amount_max: Decimal = Field(..., description="Maximum transaction amount")
    notes: Optional[str] = Field(None, description="Additional notes")


class TransactionCreate(TransactionBase):
    """Schema for creating a transaction."""

    politician_id: UUID
    asset_id: UUID
    document_id: UUID


class Transaction(TransactionBase):
    """Full transaction schema with ID."""

    id: UUID
    politician_id: UUID
    asset_id: UUID
    document_id: UUID
    created_at: datetime

    model_config = {"from_attributes": True}


class TransactionWithDetails(Transaction):
    """Transaction with related politician and asset details."""

    politician: Politician
    asset: Asset


class DocumentBase(BaseModel):
    """Base document schema."""

    document_type: DocumentTypeEnum = Field(..., description="Type of document")
    source_url: str = Field(..., description="URL of the source document")
    filing_date: date = Field(..., description="Date the document was filed")


class DocumentCreate(DocumentBase):
    """Schema for creating a document."""

    raw_content: dict = Field(..., description="Raw document content from Docling")


class Document(DocumentBase):
    """Full document schema with ID."""

    id: UUID
    processed: bool = Field(default=False, description="Whether document has been processed")
    created_at: datetime

    model_config = {"from_attributes": True}


# List response schemas
class PoliticianList(BaseModel):
    """List of politicians with pagination."""

    items: list[Politician]
    total: int
    page: int
    size: int


class TransactionList(BaseModel):
    """List of transactions with pagination."""

    items: list[TransactionWithDetails]
    total: int
    page: int
    size: int
