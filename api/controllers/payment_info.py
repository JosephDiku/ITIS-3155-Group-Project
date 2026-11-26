from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import payment_info as model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = model.PaymentInfo(
        customer_id = request.customer_id,
        card_last4 = request.card_last4,
        transaction_status = request.transaction_status,
        payment_type = request.payment_type
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return new_item

def read_all(db: Session):
    try:
        result = db.query(model.PaymentInfo).all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return result


def read_one(db: Session, payment_id):
    try:
        item = db.query(model.PaymentInfo).filter(model.PaymentInfo.id == payment_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return item


def update(db: Session, payment_id, request):
    try:
        item = db.query(model.PaymentInfo).filter(model.PaymentInfo.id == payment_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return item.first()


def delete(db: Session, payment_id):
    try:
        item = db.query(model.PaymentInfo).filter(model.PaymentInfo.id == payment_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return Response(status_code=status.HTTP_204_NO_CONTENT)
