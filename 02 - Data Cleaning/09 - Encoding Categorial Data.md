# Encoding Categorial Data
## 1. Label Encoding
### 1.1 Import Libraries
    from sklearn.preprocessing import LabelEncoder
### 1.2 Encode
    encoder = LabelEncoder() # initiate LabelEncoder
    df['column_encoded_name'] = encoder.fit_transform(df['column_to_encode_name'])
## 2. One-Hot Encoding
### 2.1 Import Libraries
    from sklearn.preprocessing import OneHotEncoder
### 2.2 Encode
    encoder = OneHotEncoder(sparse=False) # initiate 
    df_encoded = encoder.fit_transform(df[['category']])
## 3. Binary Encoding
### 3.1 Import Libraries
    import category_encoders as ce
### 3.2 Encode
    encoder = ce.BinaryEncoder(cols=['column_to_encode_name']) # initiate encoder
    df_encoded = encoder.fit_transform(df)
