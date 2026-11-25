from fastapi import APIRouter, Depends, FastAPI, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..controllers import promotions as controller
from ..schemas import promotions as schema
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/promotions",
    tags=["promotions"]
)

@router.post("/", response_model=schema.Promotion)
def create(promotion: schema.PromotionCreate, db: Session = Depends(get_db)):
    return controller.create(promotion=promotion, db=db)

@router.get("/", response_model=schema.Promotion)
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{promo_id}", response_model=schema.Promotion)
def read_one(promo_id: int, db: Session = Depends(get_db)):
    promo = controller.read_one(promo_id=promo_id, db=db)
    if promo is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promo

@router.put("/{promo_id}", response_model=schema.Promotion)
def update(promo_id: int, promotion: schema.Promotion, db: Session = Depends(get_db)):
    promo_db = controller.read_one(db, promo_id=promo_id)
    if promo_db is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return controller.update(promotion=promotion, db=db, promo_id=promo_id)

@router.delete("/{promo_id}")
def delete(promo_id: int, db: Session = Depends(get_db)):
    promo = controller.read_one(promo_id=promo_id, db=db)
    if promo is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return controller.delete(promo_id=promo_id, db=db)