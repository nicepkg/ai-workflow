# ActiveCampaign

## Basic Information

- Node Type: `nodes-base.activeCampaign`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Create and edit data in ActiveCampaign

## Available Operations

### Create
Create an account
- Value: `create`

### Delete
Delete an account
- Value: `delete`

### Get
Get data of an account
- Value: `get`

### Get Many
Get data of many accounts
- Value: `getAll`

### Update
Update an account
- Value: `update`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `value` | number | Yes | `0` | The value of the deal in cents |
| `tagType` | options | Yes | `"contact"` | Tag-type of the new tag |
| `currency` | options | Yes | `"eur"` | The currency of the deal in 3-character ISO format |
| `currency` | options | Yes | `"eur"` | The currency of the order (3-digit ISO code, e.g., "USD") |
| `name` | string | Yes | `""` | Name of the new tag |
| `tagId` | number | Yes | `0` | ID of the tag to update |
| `tagId` | number | Yes | `0` | ID of the tag to delete |
| `tagId` | number | Yes | `0` | ID of the tag to get |
| `tagId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `contactTagId` | number | Yes | `0` | ID of the contact tag to delete |

### Property Details

#### Type (`tagType`)

Tag-type of the new tag

Optional values:
- `contact`: Contact - Tag contact
- `template`: Template - Tag template

#### Currency (`currency`)

The currency of the deal in 3-character ISO format

Optional values:
- `eur`: Euro
- `usd`: United States Dollar
- `gbp`: British Pound Sterling
- `chf`: Swiss Franc
- `cny`: Renminbi
- ``: --------
- `aed`: United Arab Emirates Dirham
- `afn`: Afghan Afghani
- `all`: Albanian Lek
- `amd`: Armenian Dram
- `ang`: Netherlands Antillean Guilder
- `aoa`: Angolan Kwanza
- `ars`: Argentine Peso
- `aud`: Australian Dollar
- `awg`: Aruban Florin
- `azn`: Azerbaijani Manat
- `bam`: Bosnia-Herzegovina Convertible Mark
- `bbd`: Barbadian Dollar
- `bdt`: Bangladeshi Taka
- `bgn`: Bulgarian Lev
- `bhd`: Bahraini Dinar
- `bif`: Burundian Franc
- `bmd`: Bermudan Dollar
- `bnd`: Brunei Dollar
- `bob`: Bolivian Boliviano
- `brl`: Brazilian Real
- `bsd`: Bahamian Dollar
- `btc`: Bitcoin
- `btn`: Bhutanese Ngultrum
- `bwp`: Botswanan Pula
- `byn`: Belarusian Ruble
- `bzd`: Belize Dollar
- `cad`: Canadian Dollar
- `cdf`: Congolese Franc
- `clf`: Chilean Unit of Account (UF)
- `clp`: Chilean Peso
- `cnh`: Chinese Yuan (Offshore)
- `cop`: Colombian Peso
- `crc`: Costa Rican Colón
- `cuc`: Cuban Convertible Peso
- `cup`: Cuban Peso
- `cve`: Cape Verdean Escudo
- `czk`: Czech Republic Koruna
- `djf`: Djiboutian Franc
- `dkk`: Danish Krone
- `dop`: Dominican Peso
- `dzd`: Algerian Dinar
- `egp`: Egyptian Pound
- `ern`: Eritrean Nakfa
- `etb`: Ethiopian Birr
- `fjd`: Fijian Dollar
- `fkp`: Falkland Islands Pound
- `gel`: Georgian Lari
- `ggp`: Guernsey Pound
- `ghs`: Ghanaian Cedi
- `gip`: Gibraltar Pound
- `gmd`: Gambian Dalasi
- `gnf`: Guinean Franc
- `gtq`: Guatemalan Quetzal
- `gyd`: Guyanaese Dollar
- `hkd`: Hong Kong Dollar
- `hnl`: Honduran Lempira
- `hrk`: Croatian Kuna
- `htg`: Haitian Gourde
- `huf`: Hungarian Forint
- `idr`: Indonesian Rupiah
- `ils`: Israeli New Sheqel
- `imp`: Manx Pound
- `inr`: Indian Rupee
- `iqd`: Iraqi Dinar
- `irr`: Iranian Rial
- `isk`: Icelandic Króna
- `jep`: Jersey Pound
- `jmd`: Jamaican Dollar
- `jod`: Jordanian Dinar
- `jpy`: Japanese Yen
- `kes`: Kenyan Shilling
- `kgs`: Kyrgystani Som
- `khr`: Cambodian Riel
- `kmf`: Comorian Franc
- `kpw`: North Korean Won
- `krw`: South Korean Won
- `kwd`: Kuwaiti Dinar
- `kyd`: Cayman Islands Dollar
- `kzt`: Kazakhstani Tenge
- `lak`: Laotian Kip
- `lbp`: Lebanese Pound
- `lkr`: Sri Lankan Rupee
- `lrd`: Liberian Dollar
- `lsl`: Lesotho Loti
- `lyd`: Libyan Dinar
- `mad`: Moroccan Dirham
- `mdl`: Moldovan Leu
- `mga`: Malagasy Ariary
- `mkd`: Macedonian Denar
- `mmk`: Myanma Kyat
- `mnt`: Mongolian Tugrik
- `mop`: Macanese Pataca
- `mro`: Mauritanian Ouguiya (Pre-2018)
- `mru`: Mauritanian Ouguiya
- `mur`: Mauritian Rupee
- `mvr`: Maldivian Rufiyaa
- `mwk`: Malawian Kwacha
- `mxn`: Mexican Peso
- `myr`: Malaysian Ringgit
- `mzn`: Mozambican Metical
- `nad`: Namibian Dollar
- `ngn`: Nigerian Naira
- `nio`: Nicaraguan Córdoba
- `nok`: Norwegian Krone
- `npr`: Nepalese Rupee
- `nzd`: New Zealand Dollar
- `omr`: Omani Rial
- `pab`: Panamanian Balboa
- `pen`: Peruvian Nuevo Sol
- `pgk`: Papua New Guinean Kina
- `php`: Philippine Peso
- `pkr`: Pakistani Rupee
- `pln`: Polish Zloty
- `pyg`: Paraguayan Guarani
- `qar`: Qatari Rial
- `ron`: Romanian Leu
- `rsd`: Serbian Dinar
- `rub`: Russian Ruble
- `rwf`: Rwandan Franc
- `sar`: Saudi Riyal
- `sbd`: Solomon Islands Dollar
- `scr`: Seychellois Rupee
- `sdg`: Sudanese Pound
- `sek`: Swedish Krona
- `sgd`: Singapore Dollar
- `shp`: Saint Helena Pound
- `sll`: Sierra Leonean Leone
- `sos`: Somali Shilling
- `srd`: Surinamese Dollar
- `ssp`: South Sudanese Pound
- `std`: São Tomé and Príncipe Dobra (Pre-2018)
- `stn`: São Tomé and Príncipe Dobra
- `svc`: Salvadoran Colón
- `syp`: Syrian Pound
- `szl`: Swazi Lilangeni
- `thb`: Thai Baht
- `tjs`: Tajikistani Somoni
- `tmt`: Turkmenistani Manat
- `tnd`: Tunisian Dinar
- `top`: Tongan Pa'anga
- `try`: Turkish Lira
- `ttd`: Trinidad and Tobago Dollar
- `twd`: New Taiwan Dollar
- `tzs`: Tanzanian Shilling
- `uah`: Ukrainian Hryvnia
- `ugx`: Ugandan Shilling
- `uyu`: Uruguayan Peso
- `uzs`: Uzbekistan Som
- `vef`: Venezuelan Bolívar Fuerte
- `vnd`: Vietnamese Dong
- `vuv`: Vanuatu Vatu
- `wst`: Samoan Tala
- `xaf`: CFA Franc BEAC
- `xag`: Silver Ounce
- `xau`: Gold Ounce
- `xcd`: East Caribbean Dollar
- `xdr`: Special Drawing Rights
- `xof`: CFA Franc BCEAO
- `xpd`: Palladium Ounce
- `xpf`: CFP Franc
- `xpt`: Platinum Ounce
- `yer`: Yemeni Rial
- `zar`: South African Rand
- `zmw`: Zambian Kwacha
- `zwl`: Zimbabwean Dollar

#### Order Currency (`currency`)

The currency of the order (3-digit ISO code, e.g., "USD")

Optional values:
- `eur`: Euro
- `usd`: United States Dollar
- `gbp`: British Pound Sterling
- `chf`: Swiss Franc
- `cny`: Renminbi
- ``: --------
- `aed`: United Arab Emirates Dirham
- `afn`: Afghan Afghani
- `all`: Albanian Lek
- `amd`: Armenian Dram
- `ang`: Netherlands Antillean Guilder
- `aoa`: Angolan Kwanza
- `ars`: Argentine Peso
- `aud`: Australian Dollar
- `awg`: Aruban Florin
- `azn`: Azerbaijani Manat
- `bam`: Bosnia-Herzegovina Convertible Mark
- `bbd`: Barbadian Dollar
- `bdt`: Bangladeshi Taka
- `bgn`: Bulgarian Lev
- `bhd`: Bahraini Dinar
- `bif`: Burundian Franc
- `bmd`: Bermudan Dollar
- `bnd`: Brunei Dollar
- `bob`: Bolivian Boliviano
- `brl`: Brazilian Real
- `bsd`: Bahamian Dollar
- `btc`: Bitcoin
- `btn`: Bhutanese Ngultrum
- `bwp`: Botswanan Pula
- `byn`: Belarusian Ruble
- `bzd`: Belize Dollar
- `cad`: Canadian Dollar
- `cdf`: Congolese Franc
- `clf`: Chilean Unit of Account (UF)
- `clp`: Chilean Peso
- `cnh`: Chinese Yuan (Offshore)
- `cop`: Colombian Peso
- `crc`: Costa Rican Colón
- `cuc`: Cuban Convertible Peso
- `cup`: Cuban Peso
- `cve`: Cape Verdean Escudo
- `czk`: Czech Republic Koruna
- `djf`: Djiboutian Franc
- `dkk`: Danish Krone
- `dop`: Dominican Peso
- `dzd`: Algerian Dinar
- `egp`: Egyptian Pound
- `ern`: Eritrean Nakfa
- `etb`: Ethiopian Birr
- `fjd`: Fijian Dollar
- `fkp`: Falkland Islands Pound
- `gel`: Georgian Lari
- `ggp`: Guernsey Pound
- `ghs`: Ghanaian Cedi
- `gip`: Gibraltar Pound
- `gmd`: Gambian Dalasi
- `gnf`: Guinean Franc
- `gtq`: Guatemalan Quetzal
- `gyd`: Guyanaese Dollar
- `hkd`: Hong Kong Dollar
- `hnl`: Honduran Lempira
- `hrk`: Croatian Kuna
- `htg`: Haitian Gourde
- `huf`: Hungarian Forint
- `idr`: Indonesian Rupiah
- `ils`: Israeli New Sheqel
- `imp`: Manx Pound
- `inr`: Indian Rupee
- `iqd`: Iraqi Dinar
- `irr`: Iranian Rial
- `isk`: Icelandic Króna
- `jep`: Jersey Pound
- `jmd`: Jamaican Dollar
- `jod`: Jordanian Dinar
- `jpy`: Japanese Yen
- `kes`: Kenyan Shilling
- `kgs`: Kyrgystani Som
- `khr`: Cambodian Riel
- `kmf`: Comorian Franc
- `kpw`: North Korean Won
- `krw`: South Korean Won
- `kwd`: Kuwaiti Dinar
- `kyd`: Cayman Islands Dollar
- `kzt`: Kazakhstani Tenge
- `lak`: Laotian Kip
- `lbp`: Lebanese Pound
- `lkr`: Sri Lankan Rupee
- `lrd`: Liberian Dollar
- `lsl`: Lesotho Loti
- `lyd`: Libyan Dinar
- `mad`: Moroccan Dirham
- `mdl`: Moldovan Leu
- `mga`: Malagasy Ariary
- `mkd`: Macedonian Denar
- `mmk`: Myanma Kyat
- `mnt`: Mongolian Tugrik
- `mop`: Macanese Pataca
- `mro`: Mauritanian Ouguiya (Pre-2018)
- `mru`: Mauritanian Ouguiya
- `mur`: Mauritian Rupee
- `mvr`: Maldivian Rufiyaa
- `mwk`: Malawian Kwacha
- `mxn`: Mexican Peso
- `myr`: Malaysian Ringgit
- `mzn`: Mozambican Metical
- `nad`: Namibian Dollar
- `ngn`: Nigerian Naira
- `nio`: Nicaraguan Córdoba
- `nok`: Norwegian Krone
- `npr`: Nepalese Rupee
- `nzd`: New Zealand Dollar
- `omr`: Omani Rial
- `pab`: Panamanian Balboa
- `pen`: Peruvian Nuevo Sol
- `pgk`: Papua New Guinean Kina
- `php`: Philippine Peso
- `pkr`: Pakistani Rupee
- `pln`: Polish Zloty
- `pyg`: Paraguayan Guarani
- `qar`: Qatari Rial
- `ron`: Romanian Leu
- `rsd`: Serbian Dinar
- `rub`: Russian Ruble
- `rwf`: Rwandan Franc
- `sar`: Saudi Riyal
- `sbd`: Solomon Islands Dollar
- `scr`: Seychellois Rupee
- `sdg`: Sudanese Pound
- `sek`: Swedish Krona
- `sgd`: Singapore Dollar
- `shp`: Saint Helena Pound
- `sll`: Sierra Leonean Leone
- `sos`: Somali Shilling
- `srd`: Surinamese Dollar
- `ssp`: South Sudanese Pound
- `std`: São Tomé and Príncipe Dobra (Pre-2018)
- `stn`: São Tomé and Príncipe Dobra
- `svc`: Salvadoran Colón
- `syp`: Syrian Pound
- `szl`: Swazi Lilangeni
- `thb`: Thai Baht
- `tjs`: Tajikistani Somoni
- `tmt`: Turkmenistani Manat
- `tnd`: Tunisian Dinar
- `top`: Tongan Pa'anga
- `try`: Turkish Lira
- `ttd`: Trinidad and Tobago Dollar
- `twd`: New Taiwan Dollar
- `tzs`: Tanzanian Shilling
- `uah`: Ukrainian Hryvnia
- `ugx`: Ugandan Shilling
- `uyu`: Uruguayan Peso
- `uzs`: Uzbekistan Som
- `vef`: Venezuelan Bolívar Fuerte
- `vnd`: Vietnamese Dong
- `vuv`: Vanuatu Vatu
- `wst`: Samoan Tala
- `xaf`: CFA Franc BEAC
- `xag`: Silver Ounce
- `xau`: Gold Ounce
- `xcd`: East Caribbean Dollar
- `xdr`: Special Drawing Rights
- `xof`: CFA Franc BCEAO
- `xpd`: Palladium Ounce
- `xpf`: CFP Franc
- `xpt`: Platinum Ounce
- `yer`: Yemeni Rial
- `zar`: South African Rand
- `zmw`: Zambian Kwacha
- `zwl`: Zimbabwean Dollar

## Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
## JSON Configuration Examples

### Basic Configuration
```json
{
  "name": "ActiveCampaign",
  "type": "nodes-base.activeCampaign",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": 0,
    "tagType": "contact",
    "currency": "eur",
    "name": "",
    "tagId": "",
    "contactTagId": 0
  }
}
```

### Create Example
```json
{
  "name": "ActiveCampaign",
  "type": "nodes-base.activeCampaign",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": 0,
    "tagType": "contact",
    "currency": "eur",
    "name": "",
    "tagId": "",
    "contactTagId": 0,
    "operation": "create"
  }
}
```

### Delete Example
```json
{
  "name": "ActiveCampaign",
  "type": "nodes-base.activeCampaign",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": 0,
    "tagType": "contact",
    "currency": "eur",
    "name": "",
    "tagId": "",
    "contactTagId": 0,
    "operation": "delete"
  }
}
```
