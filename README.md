# Image Processing

### Execução

**Executar Corte Mediano**
python3 median_cut.py caminho_da_imagem qtd_cores

**Executar Método Uniforme**
python3 uniform_cut.py caminho_da_imagem qtd_cores 

### Resultados

**Métrica PSNR**

##### dog.jpg

|Cores |Corte mediano     | Método Uniforme  |
|------|------------------|------------------|
|8     |28.70354970455921 |27.907004707332803|
|32    |30.621655836762017|28.43030652544161 |
|128   |32.359868708392916|29.1510627042993  |

##### pinguim.jpg

|Cores |Corte mediano     | Método Uniforme  |
|------|------------------|------------------|
|8     |28.94771067644657 |27.885100483044916|
|32    |29.002859877869632|28.106687724779324|
|128   |29.367511714044134|29.184263826260036|
