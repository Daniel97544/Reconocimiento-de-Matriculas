# ==========================================================
# IMPORTAR LIBRERÍAS NECESARIAS
# ==========================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

# ==========================================================
# CARGAR EL CONJUNTO DE DATOS
# ==========================================================
df = pd.read_csv('/kaggle/input/diamonds/diamonds.csv')

print("Primeras filas del conjunto de datos:")
print(df.head())

print("\nForma del conjunto de datos:", df.shape)

# ==========================================================
# VERIFICAR VALORES FALTANTES Y TIPO DE DATOS
# ==========================================================
print("\nValores faltantes por columna:")
print(df.isnull().sum())

print("\nTipos de datos:")
print(df.dtypes)

# ==========================================================
# PREPROCESAMIENTO DE DATOS
# ==========================================================
# Eliminar la primera columna (índice)
df = df.drop(df.columns[0], axis=1)

# Codificar variables categóricas
label_encoder = LabelEncoder()
categorical_columns = ['cut', 'color', 'clarity']

for col in categorical_columns:
    df[col] = label_encoder.fit_transform(df[col])

print("\nDespués de codificar las variables categóricas:")
print(df.head())

# ==========================================================
# ANÁLISIS EXPLORATORIO BÁSICO
# ==========================================================
plt.figure(figsize=(10, 5))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Mapa de correlación entre las variables')
plt.show()

plt.figure(figsize=(6, 4))
sns.histplot(df['price'], kde=True, color='skyblue')
plt.title('Distribución del precio de los diamantes')
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
plt.show()

# ==========================================================
# PREPARACIÓN DE DATOS PARA EL MODELO
# ==========================================================
X = df.drop('price', axis=1)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalado de características
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Datos listos para entrenamiento.")
print("Forma del conjunto de entrenamiento:", X_train.shape)

# ==========================================================
# ENTRENAMIENTO DEL MODELO DE REGRESIÓN LINEAL
# ==========================================================
lr_model = LinearRegression()
lr_model.fit(X_train_scaled, y_train)

# Predicciones
y_pred_lr = lr_model.predict(X_test_scaled)

# Evaluación del modelo
mse = mean_squared_error(y_test, y_pred_lr)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred_lr)

print("\nResultados del modelo de Regresión Lineal:")
print(f"Error Cuadrático Medio (MSE): {mse:.2f}")
print(f"Raíz del Error Cuadrático Medio (RMSE): {rmse:.2f}")
print(f"Coeficiente de Determinación (R²): {r2:.4f}")

# ==========================================================
# AVANCE DEL PROYECTO
# ==========================================================
print("\nAVANCE DEL PROYECTO:")
print("✓ Se cargaron y analizaron los datos correctamente.")
print("✓ Se codificaron variables categóricas y se normalizaron los valores.")
print("✓ Se entrenó un modelo de Regresión Lineal con buenos resultados iniciales.")
print("✗ Próximos pasos: incluir modelo SVM y comparación entre modelos.")

