import numpy as np

def calculate(list):
    import numpy as np
    # 1. التحقق من أن القائمة تحتوي على 9 عناصر
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # 2. تحويل القائمة إلى مصفوفة Numpy بأبعاد 3x3
    matrix = np.array(list).reshape(3, 3)

    # 3. حساب القيم على الأعمدة (axis=0) والصفوف (axis=1) والمصفوفة المسطحة (flattened)
    # ملاحظة: يتم استخدام tolist() لأن المطلوب إرجاع قائمة وليس NumPy Array
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.mean().item()
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().item()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().item()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().item()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().item()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().item()
        ]
    }

    return calculations
