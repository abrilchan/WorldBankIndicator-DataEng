# WorldBankIndicator-DataEng

### Large Coding Test for Data Engineer

Este proyecto fue realizado como parte del proceso de reclutamiento de [Ventagium](https://www.ventagium.com/). El respositorio contiene un Pipeline cuyo propósito es extraer los datos correspondientes al total de población de cada país a través de los años usando la [API JSON](http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json) de [Indicadores del Banco Mundial](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation).


## BoilerPlate

```text
.WorldBankIndicator-DataEng
├── README.md
├── lib
|  ├── __init__.py
|  ├── dataframe_indicators.py
|  ├── getting_data.py
|  ├── series_countries.py
|  ├── series_iso.py
|  ├── series_years.py
└── growth_analysis
   └── growth_per_country.py
├── Notebooks
|  ├── WorldBank_Pipeline_Large.ipynb
|  ├── WorldBank_Pipeline.ipynb
```

[WorldBank_Pipeline_Large](Notebooks/WorldBank_Pipeline_Large.ipynb) contiene una Notebook con el proceso lógico que se siguió para completar el proyecto.
<br>
El directorio [lib](lib) contiene el código modularizado.
[WorldBank_Pipeline](Notebooks/WorldBank_Pipeline.ipynb) contiene una Notebook con el proceso para presentar la información.

