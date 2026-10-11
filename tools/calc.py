from langchain.tools import tool


@tool
def calc_total_cost(
    device_price: int,
    monthly_fee: int,
    months: int = 24,
    discount: int = 0,
) -> dict:
    """端末代と月額料金から、指定した月数の総額を計算する。

    Args:
        device_price: 端末代（円）。今の端末を使うなら0。
        monthly_fee: 月額料金（円）。
        months: 利用月数。
        discount: 割引やポイント還元の合計（円）。
    """
    total = device_price + monthly_fee * months - discount
    return {
        "total": total,
        "monthly_average": round(total / months),
        "formula": f"{device_price} + {monthly_fee} x {months} - {discount} = {total}",
    }
