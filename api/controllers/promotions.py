from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import promotions as model
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, promotion):
    new_promo = model.Promotion(
        promo_code = promotion.promo_code,
        expiration_date = promotion.expiration_date
    )
    try:
        db.add(new_promo)
        db.commit()
        db.refresh(new_promo)
    except SQLAlchemyError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
    return new_promo

def read_all(db: Session):
    try:
        result = db.query(model.Promotion).all()
    except SQLAlchemyError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
    return result

def read_one(db: Session, promo_id: int):
    try:
        result = db.query(model.Promotion).filter(model.Promotion.id == promo_id).first()
    except SQLAlchemyError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
    return result

def update(db: Session, promo_id: int, promotion):
    try:
        db_promo = db.query(model.Promotion).filter(model.Promotion.id == promo_id)
    except SQLAlchemyError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))

    try:
        update_data = promotion.model_dump(exclude_unset=True)
    except SQLAlchemyError as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

    try:
        db_promo.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
    return db_promo.first()

def delete(db: Session, promo_id: int):
    try:
        db_promo = db.query(model.Promotion).filter(model.Promotion.id == promo_id)
    except SQLAlchemyError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))
    try:
        db_promo.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
    return Response(status_code=status.HTTP_204_NO_CONTENT)
