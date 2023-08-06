"""
Copyright 2019 Goldman Sachs.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
"""

from enum import Enum
from gs_quant.base import Base, EnumBase, get_enum_value
from gs_quant.target.common import *
from typing import Tuple, Union
import datetime


class AssetClass(EnumBase, Enum):    
    
    """Asset classification of security. Assets are classified into broad groups which exhibit similar characteristics and behave in a consistent way under different market conditions"""

    Cash = 'Cash'
    Commod = 'Commod'
    Credit = 'Credit'
    Cross_Asset = 'Cross Asset'
    Equity = 'Equity'
    Fund = 'Fund'
    FX = 'FX'
    Mortgage = 'Mortgage'
    Rates = 'Rates'
    Loan = 'Loan'
    
    def __repr__(self):
        return self.value


class AssetType(EnumBase, Enum):    
    
    """Asset type differentiates the product categorization or contract type"""

    Access = 'Access'
    Basis = 'Basis'
    BasisSwap = 'BasisSwap'
    Benchmark = 'Benchmark'
    Benchmark_Rate = 'Benchmark Rate'
    Bond = 'Bond'
    Calendar_Spread = 'Calendar Spread'
    Cap = 'Cap'
    Cash = 'Cash'
    Certificate = 'Certificate'
    CD = 'CD'
    Cliquet = 'Cliquet'
    Commodity = 'Commodity'
    Company = 'Company'
    Convertible = 'Convertible'
    Credit_Basket = 'Credit Basket'
    Cross = 'Cross'
    Crypto_Currency = 'Crypto Currency'
    Currency = 'Currency'
    Custom_Basket = 'Custom Basket'
    Default_Swap = 'Default Swap'
    Economic = 'Economic'
    Endowment = 'Endowment'
    Equity_Basket = 'Equity Basket'
    ETF = 'ETF'
    ETN = 'ETN'
    Event = 'Event'
    Fixing = 'Fixing'
    Floor = 'Floor'
    Forward = 'Forward'
    Future = 'Future'
    Hedge_Fund = 'Hedge Fund'
    Index = 'Index'
    Inter_Commodity_Spread = 'Inter-Commodity Spread'
    Market_Location = 'Market Location'
    Multi_Asset_Allocation = 'Multi-Asset Allocation'
    Mutual_Fund = 'Mutual Fund'
    Note = 'Note'
    Option = 'Option'
    Pension_Fund = 'Pension Fund'
    Preferred_Stock = 'Preferred Stock'
    Physical = 'Physical'
    Reference_Entity = 'Reference Entity'
    Research_Basket = 'Research Basket'
    Rate = 'Rate'
    Risk_Premia = 'Risk Premia'
    Securities_Lending_Loan = 'Securities Lending Loan'
    Share_Class = 'Share Class'
    Single_Stock = 'Single Stock'
    Swap = 'Swap'
    Swaption = 'Swaption'
    Systematic_Hedging = 'Systematic Hedging'
    
    def __repr__(self):
        return self.value


class Format(EnumBase, Enum):    
    
    """Alternative format for data to be returned in"""

    Json = 'Json'
    Excel = 'Excel'
    MessagePack = 'MessagePack'
    Pdf = 'Pdf'
    
    def __repr__(self):
        return self.value


class MarketDataFrequency(EnumBase, Enum):    
    
    Real_Time = 'Real Time'
    End_Of_Day = 'End Of Day'
    
    def __repr__(self):
        return self.value


class MarketDataMeasure(EnumBase, Enum):    
    
    Last = 'Last'
    Curve = 'Curve'
    Close_Change = 'Close Change'
    Previous_Close = 'Previous Close'
    
    def __repr__(self):
        return self.value


class MarketDataVendor(EnumBase, Enum):    
    
    Goldman_Sachs = 'Goldman Sachs'
    Thomson_Reuters = 'Thomson Reuters'
    Solactive = 'Solactive'
    Bloomberg = 'Bloomberg'
    Axioma = 'Axioma'
    Goldman_Sachs_Prime_Services = 'Goldman Sachs Prime Services'
    Goldman_Sachs_Global_Investment_Research = 'Goldman Sachs Global Investment Research'
    National_Weather_Service = 'National Weather Service'
    WM = 'WM'
    Hedge_Fund_Research__Inc_ = 'Hedge Fund Research, Inc.'
    London_Stock_Exchange = 'London Stock Exchange'
    Goldman_Sachs_MDFarm = 'Goldman Sachs MDFarm'
    
    def __repr__(self):
        return self.value


class MeasureEntityType(EnumBase, Enum):    
    
    """Entity type associated with a measure."""

    ASSET = 'ASSET'
    BACKTEST = 'BACKTEST'
    KPI = 'KPI'
    
    def __repr__(self):
        return self.value


class AdvancedFilter(Base):
        
    """Advanced filter for numeric fields."""
       
    def __init__(self, column: str, value: float, operator: str):
        super().__init__()
        self.__column = column
        self.__value = value
        self.__operator = operator

    @property
    def column(self) -> str:
        """Database column to filter on."""
        return self.__column

    @column.setter
    def column(self, value: str):
        self.__column = value
        self._property_changed('column')        

    @property
    def value(self) -> float:
        """Value to compare against."""
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value
        self._property_changed('value')        

    @property
    def operator(self) -> str:
        """Comparison operator."""
        return self.__operator

    @operator.setter
    def operator(self, value: str):
        self.__operator = value
        self._property_changed('operator')        


class DataFilter(Base):
        
    """Filter on specified field."""
       
    def __init__(self, field: str, values: Tuple[str, ...], column: str = None):
        super().__init__()
        self.__field = field
        self.__column = column
        self.__values = values

    @property
    def field(self) -> str:
        """Field to filter on."""
        return self.__field

    @field.setter
    def field(self, value: str):
        self.__field = value
        self._property_changed('field')        

    @property
    def column(self) -> str:
        """Database column name."""
        return self.__column

    @column.setter
    def column(self, value: str):
        self.__column = value
        self._property_changed('column')        

    @property
    def values(self) -> Tuple[str, ...]:
        """Value(s) to match."""
        return self.__values

    @values.setter
    def values(self, value: Tuple[str, ...]):
        self.__values = value
        self._property_changed('values')        


class DataSetDefaults(Base):
        
    """Default settings."""
       
    def __init__(self, startSeconds: float = None, endSeconds: float = None, delaySeconds: float = None):
        super().__init__()
        self.__startSeconds = startSeconds
        self.__endSeconds = endSeconds
        self.__delaySeconds = delaySeconds

    @property
    def startSeconds(self) -> float:
        """Default start date/time, in seconds before current time."""
        return self.__startSeconds

    @startSeconds.setter
    def startSeconds(self, value: float):
        self.__startSeconds = value
        self._property_changed('startSeconds')        

    @property
    def endSeconds(self) -> float:
        """Default end date/time, in seconds before current time."""
        return self.__endSeconds

    @endSeconds.setter
    def endSeconds(self, value: float):
        self.__endSeconds = value
        self._property_changed('endSeconds')        

    @property
    def delaySeconds(self) -> float:
        """Default market delay to apply, in seconds."""
        return self.__delaySeconds

    @delaySeconds.setter
    def delaySeconds(self, value: float):
        self.__delaySeconds = value
        self._property_changed('delaySeconds')        


class EntitlementExclusions(Base):
        
    """Defines the exclusion entitlements of a given resource"""
       
    def __init__(self, view: Tuple[Tuple[str, ...], ...] = None, edit: Tuple[Tuple[str, ...], ...] = None, admin: Tuple[Tuple[str, ...], ...] = None, rebalance: Tuple[Tuple[str, ...], ...] = None, trade: Tuple[Tuple[str, ...], ...] = None, upload: Tuple[Tuple[str, ...], ...] = None, query: Tuple[Tuple[str, ...], ...] = None, performanceDetails: Tuple[Tuple[str, ...], ...] = None, plot: Tuple[Tuple[str, ...], ...] = None):
        super().__init__()
        self.__view = view
        self.__edit = edit
        self.__admin = admin
        self.__rebalance = rebalance
        self.__trade = trade
        self.__upload = upload
        self.__query = query
        self.__performanceDetails = performanceDetails
        self.__plot = plot

    @property
    def view(self) -> Tuple[Tuple[str, ...], ...]:
        return self.__view

    @view.setter
    def view(self, value: Tuple[Tuple[str, ...], ...]):
        self.__view = value
        self._property_changed('view')        

    @property
    def edit(self) -> Tuple[Tuple[str, ...], ...]:
        return self.__edit

    @edit.setter
    def edit(self, value: Tuple[Tuple[str, ...], ...]):
        self.__edit = value
        self._property_changed('edit')        

    @property
    def admin(self) -> Tuple[Tuple[str, ...], ...]:
        return self.__admin

    @admin.setter
    def admin(self, value: Tuple[Tuple[str, ...], ...]):
        self.__admin = value
        self._property_changed('admin')        

    @property
    def rebalance(self) -> Tuple[Tuple[str, ...], ...]:
        return self.__rebalance

    @rebalance.setter
    def rebalance(self, value: Tuple[Tuple[str, ...], ...]):
        self.__rebalance = value
        self._property_changed('rebalance')        

    @property
    def trade(self) -> Tuple[Tuple[str, ...], ...]:
        return self.__trade

    @trade.setter
    def trade(self, value: Tuple[Tuple[str, ...], ...]):
        self.__trade = value
        self._property_changed('trade')        

    @property
    def upload(self) -> Tuple[Tuple[str, ...], ...]:
        return self.__upload

    @upload.setter
    def upload(self, value: Tuple[Tuple[str, ...], ...]):
        self.__upload = value
        self._property_changed('upload')        

    @property
    def query(self) -> Tuple[Tuple[str, ...], ...]:
        return self.__query

    @query.setter
    def query(self, value: Tuple[Tuple[str, ...], ...]):
        self.__query = value
        self._property_changed('query')        

    @property
    def performanceDetails(self) -> Tuple[Tuple[str, ...], ...]:
        return self.__performanceDetails

    @performanceDetails.setter
    def performanceDetails(self, value: Tuple[Tuple[str, ...], ...]):
        self.__performanceDetails = value
        self._property_changed('performanceDetails')        

    @property
    def plot(self) -> Tuple[Tuple[str, ...], ...]:
        return self.__plot

    @plot.setter
    def plot(self, value: Tuple[Tuple[str, ...], ...]):
        self.__plot = value
        self._property_changed('plot')        


class Entitlements(Base):
        
    """Defines the entitlements of a given resource"""
       
    def __init__(self, view: Tuple[str, ...] = None, edit: Tuple[str, ...] = None, admin: Tuple[str, ...] = None, rebalance: Tuple[str, ...] = None, trade: Tuple[str, ...] = None, upload: Tuple[str, ...] = None, query: Tuple[str, ...] = None, performanceDetails: Tuple[str, ...] = None, plot: Tuple[str, ...] = None):
        super().__init__()
        self.__view = view
        self.__edit = edit
        self.__admin = admin
        self.__rebalance = rebalance
        self.__trade = trade
        self.__upload = upload
        self.__query = query
        self.__performanceDetails = performanceDetails
        self.__plot = plot

    @property
    def view(self) -> Tuple[str, ...]:
        """Permission to view the resource and its contents"""
        return self.__view

    @view.setter
    def view(self, value: Tuple[str, ...]):
        self.__view = value
        self._property_changed('view')        

    @property
    def edit(self) -> Tuple[str, ...]:
        """Permission to edit details about the resource content, excluding entitlements. Can also delete the resource"""
        return self.__edit

    @edit.setter
    def edit(self, value: Tuple[str, ...]):
        self.__edit = value
        self._property_changed('edit')        

    @property
    def admin(self) -> Tuple[str, ...]:
        """Permission to edit all details of the resource, including entitlements. Can also delete the resource"""
        return self.__admin

    @admin.setter
    def admin(self, value: Tuple[str, ...]):
        self.__admin = value
        self._property_changed('admin')        

    @property
    def rebalance(self) -> Tuple[str, ...]:
        """Permission to rebalance the constituent weights of the resource"""
        return self.__rebalance

    @rebalance.setter
    def rebalance(self, value: Tuple[str, ...]):
        self.__rebalance = value
        self._property_changed('rebalance')        

    @property
    def trade(self) -> Tuple[str, ...]:
        """Permission to trade the resource"""
        return self.__trade

    @trade.setter
    def trade(self, value: Tuple[str, ...]):
        self.__trade = value
        self._property_changed('trade')        

    @property
    def upload(self) -> Tuple[str, ...]:
        """Permission to upload data to the given resource"""
        return self.__upload

    @upload.setter
    def upload(self, value: Tuple[str, ...]):
        self.__upload = value
        self._property_changed('upload')        

    @property
    def query(self) -> Tuple[str, ...]:
        """Permission to query data from the given resource"""
        return self.__query

    @query.setter
    def query(self, value: Tuple[str, ...]):
        self.__query = value
        self._property_changed('query')        

    @property
    def performanceDetails(self) -> Tuple[str, ...]:
        """Permission to view the resource, it's entire contents, and related data"""
        return self.__performanceDetails

    @performanceDetails.setter
    def performanceDetails(self, value: Tuple[str, ...]):
        self.__performanceDetails = value
        self._property_changed('performanceDetails')        

    @property
    def plot(self) -> Tuple[str, ...]:
        """Permission to plot data from the given resource"""
        return self.__plot

    @plot.setter
    def plot(self, value: Tuple[str, ...]):
        self.__plot = value
        self._property_changed('plot')        


class FieldColumnPair(Base):
        
    """Map from fields to database columns."""
       
    def __init__(self, field: str = None, column: str = None, fieldDescription: str = None):
        super().__init__()
        self.__field = field
        self.__column = column
        self.__fieldDescription = fieldDescription

    @property
    def field(self) -> str:
        """Field name."""
        return self.__field

    @field.setter
    def field(self, value: str):
        self.__field = value
        self._property_changed('field')        

    @property
    def column(self) -> str:
        """Database column name."""
        return self.__column

    @column.setter
    def column(self, value: str):
        self.__column = value
        self._property_changed('column')        

    @property
    def fieldDescription(self) -> str:
        """Custom description (overrides field default)."""
        return self.__fieldDescription

    @fieldDescription.setter
    def fieldDescription(self, value: str):
        self.__fieldDescription = value
        self._property_changed('fieldDescription')        


class HistoryFilter(Base):
        
    """Restricts queries against dataset to an absolute or relative range."""
       
    def __init__(self, absoluteStart: datetime.datetime = None, absoluteEnd: datetime.datetime = None, relativeStartSeconds: float = None, relativeEndSeconds: float = None):
        super().__init__()
        self.__absoluteStart = absoluteStart
        self.__absoluteEnd = absoluteEnd
        self.__relativeStartSeconds = relativeStartSeconds
        self.__relativeEndSeconds = relativeEndSeconds

    @property
    def absoluteStart(self) -> datetime.datetime:
        """ISO 8601-formatted timestamp"""
        return self.__absoluteStart

    @absoluteStart.setter
    def absoluteStart(self, value: datetime.datetime):
        self.__absoluteStart = value
        self._property_changed('absoluteStart')        

    @property
    def absoluteEnd(self) -> datetime.datetime:
        """ISO 8601-formatted timestamp"""
        return self.__absoluteEnd

    @absoluteEnd.setter
    def absoluteEnd(self, value: datetime.datetime):
        self.__absoluteEnd = value
        self._property_changed('absoluteEnd')        

    @property
    def relativeStartSeconds(self) -> float:
        """Earliest start time in seconds before current time."""
        return self.__relativeStartSeconds

    @relativeStartSeconds.setter
    def relativeStartSeconds(self, value: float):
        self.__relativeStartSeconds = value
        self._property_changed('relativeStartSeconds')        

    @property
    def relativeEndSeconds(self) -> float:
        """Latest end time in seconds before current time."""
        return self.__relativeEndSeconds

    @relativeEndSeconds.setter
    def relativeEndSeconds(self, value: float):
        self.__relativeEndSeconds = value
        self._property_changed('relativeEndSeconds')        


class MDAPI(Base):
        
    """Defines MDAPI fields."""
       
    def __init__(self, type: str, quotingStyles: Tuple[dict, ...], class_: str = None):
        super().__init__()
        self.__class = class_
        self.__type = type
        self.__quotingStyles = quotingStyles

    @property
    def class_(self) -> str:
        """MDAPI Class."""
        return self.__class

    @class_.setter
    def class_(self, value: str):
        self.__class = value
        self._property_changed('class')        

    @property
    def type(self) -> str:
        """The MDAPI Type field (private)"""
        return self.__type

    @type.setter
    def type(self, value: str):
        self.__type = value
        self._property_changed('type')        

    @property
    def quotingStyles(self) -> Tuple[dict, ...]:
        """Map from MDAPI QuotingStyles to database columns"""
        return self.__quotingStyles

    @quotingStyles.setter
    def quotingStyles(self, value: Tuple[dict, ...]):
        self.__quotingStyles = value
        self._property_changed('quotingStyles')        


class MarketDataCoordinate(Base):
        
    """Object representation of a market data coordinate"""
       
    def __init__(self, marketDataType: str, assetId: str = None, marketDataAsset: str = None, pointClass: str = None, marketDataPoint: Tuple[str, ...] = None, field: str = None, quotingStyle: str = None):
        super().__init__()
        self.__marketDataType = marketDataType
        self.__assetId = assetId
        self.__marketDataAsset = marketDataAsset
        self.__pointClass = pointClass
        self.__marketDataPoint = marketDataPoint
        self.__field = field
        self.__quotingStyle = quotingStyle

    @property
    def marketDataType(self) -> str:
        """The Market Data Type, e.g. IR, IR_BASIS, FX, FX_Vol"""
        return self.__marketDataType

    @marketDataType.setter
    def marketDataType(self, value: str):
        self.__marketDataType = value
        self._property_changed('marketDataType')        

    @property
    def assetId(self) -> str:
        """Marquee unique asset identifier."""
        return self.__assetId

    @assetId.setter
    def assetId(self, value: str):
        self.__assetId = value
        self._property_changed('assetId')        

    @property
    def marketDataAsset(self) -> str:
        """The specific aaset, e.g. USD, EUR-EURIBOR-Telerate, WTI"""
        return self.__marketDataAsset

    @marketDataAsset.setter
    def marketDataAsset(self, value: str):
        self.__marketDataAsset = value
        self._property_changed('marketDataAsset')        

    @property
    def pointClass(self) -> str:
        """The market data pointClass, e.g. Swap, Cash."""
        return self.__pointClass

    @pointClass.setter
    def pointClass(self, value: str):
        self.__pointClass = value
        self._property_changed('pointClass')        

    @property
    def marketDataPoint(self) -> Tuple[str, ...]:
        """The specific point, e.g. 3m, 10y, 11y, Dec19"""
        return self.__marketDataPoint

    @marketDataPoint.setter
    def marketDataPoint(self, value: Tuple[str, ...]):
        self.__marketDataPoint = value
        self._property_changed('marketDataPoint')        

    @property
    def field(self) -> str:
        """The specific field: bid, mid, rate etc"""
        return self.__field

    @field.setter
    def field(self, value: str):
        self.__field = value
        self._property_changed('field')        

    @property
    def quotingStyle(self) -> str:
        return self.__quotingStyle

    @quotingStyle.setter
    def quotingStyle(self, value: str):
        self.__quotingStyle = value
        self._property_changed('quotingStyle')        


class MarketDataField(Base):
               
    def __init__(self, name: str = None, mapping: str = None):
        super().__init__()
        self.__name = name
        self.__mapping = mapping

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value
        self._property_changed('name')        

    @property
    def mapping(self) -> str:
        return self.__mapping

    @mapping.setter
    def mapping(self, value: str):
        self.__mapping = value
        self._property_changed('mapping')        


class MarketDataFilteredField(Base):
               
    def __init__(self, field: str = None, defaultValue: str = None, defaultNumericalValue: float = None, numericalValues: Tuple[float, ...] = None, values: Tuple[str, ...] = None):
        super().__init__()
        self.__field = field
        self.__defaultValue = defaultValue
        self.__defaultNumericalValue = defaultNumericalValue
        self.__numericalValues = numericalValues
        self.__values = values

    @property
    def field(self) -> str:
        """Filtered field name"""
        return self.__field

    @field.setter
    def field(self, value: str):
        self.__field = value
        self._property_changed('field')        

    @property
    def defaultValue(self) -> str:
        """Default filtered field"""
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, value: str):
        self.__defaultValue = value
        self._property_changed('defaultValue')        

    @property
    def defaultNumericalValue(self) -> float:
        """Default numerical filtered field"""
        return self.__defaultNumericalValue

    @defaultNumericalValue.setter
    def defaultNumericalValue(self, value: float):
        self.__defaultNumericalValue = value
        self._property_changed('defaultNumericalValue')        

    @property
    def numericalValues(self) -> Tuple[float, ...]:
        """Array of numerical filtered fields"""
        return self.__numericalValues

    @numericalValues.setter
    def numericalValues(self, value: Tuple[float, ...]):
        self.__numericalValues = value
        self._property_changed('numericalValues')        

    @property
    def values(self) -> Tuple[str, ...]:
        """Array of filtered fields"""
        return self.__values

    @values.setter
    def values(self, value: Tuple[str, ...]):
        self.__values = value
        self._property_changed('values')        


class MeasureBacktest(Base):
        
    """Describes backtests that should be associated with a measure."""
       
    def __init__(self, ):
        super().__init__()
        


class MeasureKpi(Base):
        
    """Describes KPIs that should be associated with a measure."""
       
    def __init__(self, ):
        super().__init__()
        


class MidPrice(Base):
        
    """Specification for a mid price column derived from bid and ask columns."""
       
    def __init__(self, bidColumn: str = None, askColumn: str = None, midColumn: str = None):
        super().__init__()
        self.__bidColumn = bidColumn
        self.__askColumn = askColumn
        self.__midColumn = midColumn

    @property
    def bidColumn(self) -> str:
        """Database column name."""
        return self.__bidColumn

    @bidColumn.setter
    def bidColumn(self, value: str):
        self.__bidColumn = value
        self._property_changed('bidColumn')        

    @property
    def askColumn(self) -> str:
        """Database column name."""
        return self.__askColumn

    @askColumn.setter
    def askColumn(self, value: str):
        self.__askColumn = value
        self._property_changed('askColumn')        

    @property
    def midColumn(self) -> str:
        """Database column name."""
        return self.__midColumn

    @midColumn.setter
    def midColumn(self, value: str):
        self.__midColumn = value
        self._property_changed('midColumn')        


class Op(Base):
        
    """Operations for searches."""
       
    def __init__(self, gte: Union[datetime.date, float] = None, lte: Union[datetime.date, float] = None, lt: Union[datetime.date, float] = None, gt: Union[datetime.date, float] = None):
        super().__init__()
        self.__gte = gte
        self.__lte = lte
        self.__lt = lt
        self.__gt = gt

    @property
    def gte(self) -> Union[datetime.date, float]:
        """search for values greater than or equal."""
        return self.__gte

    @gte.setter
    def gte(self, value: Union[datetime.date, float]):
        self.__gte = value
        self._property_changed('gte')        

    @property
    def lte(self) -> Union[datetime.date, float]:
        """search for values less than or equal to."""
        return self.__lte

    @lte.setter
    def lte(self, value: Union[datetime.date, float]):
        self.__lte = value
        self._property_changed('lte')        

    @property
    def lt(self) -> Union[datetime.date, float]:
        """search for values less than."""
        return self.__lt

    @lt.setter
    def lt(self, value: Union[datetime.date, float]):
        self.__lt = value
        self._property_changed('lt')        

    @property
    def gt(self) -> Union[datetime.date, float]:
        """search for values greater than."""
        return self.__gt

    @gt.setter
    def gt(self, value: Union[datetime.date, float]):
        self.__gt = value
        self._property_changed('gt')        


class ParserEntity(Base):
        
    """Settings for a parser processor"""
       
    def __init__(self, onlyNormalizedFields: bool = None, quotes: bool = None, trades: bool = None):
        super().__init__()
        self.__onlyNormalizedFields = onlyNormalizedFields
        self.__quotes = quotes
        self.__trades = trades

    @property
    def onlyNormalizedFields(self) -> bool:
        """Setting for onlyNormalizedFields."""
        return self.__onlyNormalizedFields

    @onlyNormalizedFields.setter
    def onlyNormalizedFields(self, value: bool):
        self.__onlyNormalizedFields = value
        self._property_changed('onlyNormalizedFields')        

    @property
    def quotes(self) -> bool:
        """Setting for quotes."""
        return self.__quotes

    @quotes.setter
    def quotes(self, value: bool):
        self.__quotes = value
        self._property_changed('quotes')        

    @property
    def trades(self) -> bool:
        """Setting for trades."""
        return self.__trades

    @trades.setter
    def trades(self, value: bool):
        self.__trades = value
        self._property_changed('trades')        


class ComplexFilter(Base):
        
    """A compound filter for data requests."""
       
    def __init__(self, operator: str, simpleFilters: Tuple[DataFilter, ...]):
        super().__init__()
        self.__operator = operator
        self.__simpleFilters = simpleFilters

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, value: str):
        self.__operator = value
        self._property_changed('operator')        

    @property
    def simpleFilters(self) -> Tuple[DataFilter, ...]:
        """Filter on specified field."""
        return self.__simpleFilters

    @simpleFilters.setter
    def simpleFilters(self, value: Tuple[DataFilter, ...]):
        self.__simpleFilters = value
        self._property_changed('simpleFilters')        


class DataSetDimensions(Base):
        
    """Dataset dimensions."""
       
    def __init__(self, timeField: str, transactionTimeField: str = None, symbolDimensions: Tuple[str, ...] = None, nonSymbolDimensions: Tuple[FieldColumnPair, ...] = None, keyDimensions: Tuple[str, ...] = None, measures: Tuple[FieldColumnPair, ...] = None, entityDimension: str = None):
        super().__init__()
        self.__timeField = timeField
        self.__transactionTimeField = transactionTimeField
        self.__symbolDimensions = symbolDimensions
        self.__nonSymbolDimensions = nonSymbolDimensions
        self.__keyDimensions = keyDimensions
        self.__measures = measures
        self.__entityDimension = entityDimension

    @property
    def timeField(self) -> str:
        return self.__timeField

    @timeField.setter
    def timeField(self, value: str):
        self.__timeField = value
        self._property_changed('timeField')        

    @property
    def transactionTimeField(self) -> str:
        """For bi-temporal datasets, field for capturing the time at which a data point was updated."""
        return self.__transactionTimeField

    @transactionTimeField.setter
    def transactionTimeField(self, value: str):
        self.__transactionTimeField = value
        self._property_changed('transactionTimeField')        

    @property
    def symbolDimensions(self) -> Tuple[str, ...]:
        """Set of fields that determine database table name."""
        return self.__symbolDimensions

    @symbolDimensions.setter
    def symbolDimensions(self, value: Tuple[str, ...]):
        self.__symbolDimensions = value
        self._property_changed('symbolDimensions')        

    @property
    def nonSymbolDimensions(self) -> Tuple[FieldColumnPair, ...]:
        """Fields that are not nullable."""
        return self.__nonSymbolDimensions

    @nonSymbolDimensions.setter
    def nonSymbolDimensions(self, value: Tuple[FieldColumnPair, ...]):
        self.__nonSymbolDimensions = value
        self._property_changed('nonSymbolDimensions')        

    @property
    def keyDimensions(self) -> Tuple[str, ...]:
        return self.__keyDimensions

    @keyDimensions.setter
    def keyDimensions(self, value: Tuple[str, ...]):
        self.__keyDimensions = value
        self._property_changed('keyDimensions')        

    @property
    def measures(self) -> Tuple[FieldColumnPair, ...]:
        """Fields that are nullable."""
        return self.__measures

    @measures.setter
    def measures(self, value: Tuple[FieldColumnPair, ...]):
        self.__measures = value
        self._property_changed('measures')        

    @property
    def entityDimension(self) -> str:
        """Symbol dimension corresponding to an entity e.g. asset or report."""
        return self.__entityDimension

    @entityDimension.setter
    def entityDimension(self, value: str):
        self.__entityDimension = value
        self._property_changed('entityDimension')        


class DataSetParameters(Base):
        
    """Dataset parameters."""
       
    def __init__(self, uploadDataPolicy: str, logicalDb: str, symbolStrategy: str, applyMarketDataEntitlements: bool, coverage: str, frequency: str, methodology: str, history: str, category: str = None, subCategory: str = None, assetClass: Union[AssetClass, str] = None, ownerIds: Tuple[str, ...] = None, approverIds: Tuple[str, ...] = None, supportIds: Tuple[str, ...] = None, supportDistributionList: Tuple[str, ...] = None, identifierMapperName: str = None, constantSymbols: Tuple[str, ...] = None, underlyingDataSetId: str = None, immutable: bool = None, includeInCatalog: bool = None, overrideQueryColumnIds: Tuple[str, ...] = None, plot: bool = None, coverageEnabled: bool = True):
        super().__init__()
        self.__category = category
        self.__subCategory = subCategory
        self.__methodology = methodology
        self.__coverage = coverage
        self.__history = history
        self.__frequency = frequency
        self.__assetClass = assetClass if isinstance(assetClass, AssetClass) else get_enum_value(AssetClass, assetClass)
        self.__ownerIds = ownerIds
        self.__approverIds = approverIds
        self.__supportIds = supportIds
        self.__supportDistributionList = supportDistributionList
        self.__applyMarketDataEntitlements = applyMarketDataEntitlements
        self.__uploadDataPolicy = uploadDataPolicy
        self.__identifierMapperName = identifierMapperName
        self.__logicalDb = logicalDb
        self.__symbolStrategy = symbolStrategy
        self.__constantSymbols = constantSymbols
        self.__underlyingDataSetId = underlyingDataSetId
        self.__immutable = immutable
        self.__includeInCatalog = includeInCatalog
        self.__overrideQueryColumnIds = overrideQueryColumnIds
        self.__plot = plot
        self.__coverageEnabled = coverageEnabled

    @property
    def category(self) -> str:
        """Top level grouping."""
        return self.__category

    @category.setter
    def category(self, value: str):
        self.__category = value
        self._property_changed('category')        

    @property
    def subCategory(self) -> str:
        """Second level grouping."""
        return self.__subCategory

    @subCategory.setter
    def subCategory(self, value: str):
        self.__subCategory = value
        self._property_changed('subCategory')        

    @property
    def methodology(self) -> str:
        """Methodology of dataset."""
        return self.__methodology

    @methodology.setter
    def methodology(self, value: str):
        self.__methodology = value
        self._property_changed('methodology')        

    @property
    def coverage(self) -> str:
        """Coverage of dataset."""
        return self.__coverage

    @coverage.setter
    def coverage(self, value: str):
        self.__coverage = value
        self._property_changed('coverage')        

    @property
    def history(self) -> str:
        """Period of time covered by dataset."""
        return self.__history

    @history.setter
    def history(self, value: str):
        self.__history = value
        self._property_changed('history')        

    @property
    def frequency(self) -> str:
        """Frequency of updates to dataset."""
        return self.__frequency

    @frequency.setter
    def frequency(self, value: str):
        self.__frequency = value
        self._property_changed('frequency')        

    @property
    def assetClass(self) -> Union[AssetClass, str]:
        """Asset classification of security. Assets are classified into broad groups which exhibit similar characteristics and behave in a consistent way under different market conditions"""
        return self.__assetClass

    @assetClass.setter
    def assetClass(self, value: Union[AssetClass, str]):
        self.__assetClass = value if isinstance(value, AssetClass) else get_enum_value(AssetClass, value)
        self._property_changed('assetClass')        

    @property
    def ownerIds(self) -> Tuple[str, ...]:
        """Users who own dataset."""
        return self.__ownerIds

    @ownerIds.setter
    def ownerIds(self, value: Tuple[str, ...]):
        self.__ownerIds = value
        self._property_changed('ownerIds')        

    @property
    def approverIds(self) -> Tuple[str, ...]:
        """Users who can grant access to dataset."""
        return self.__approverIds

    @approverIds.setter
    def approverIds(self, value: Tuple[str, ...]):
        self.__approverIds = value
        self._property_changed('approverIds')        

    @property
    def supportIds(self) -> Tuple[str, ...]:
        """Users who support dataset."""
        return self.__supportIds

    @supportIds.setter
    def supportIds(self, value: Tuple[str, ...]):
        self.__supportIds = value
        self._property_changed('supportIds')        

    @property
    def supportDistributionList(self) -> Tuple[str, ...]:
        """Distribution list who support dataset."""
        return self.__supportDistributionList

    @supportDistributionList.setter
    def supportDistributionList(self, value: Tuple[str, ...]):
        self.__supportDistributionList = value
        self._property_changed('supportDistributionList')        

    @property
    def applyMarketDataEntitlements(self) -> bool:
        """Whether market data entitlements are checked."""
        return self.__applyMarketDataEntitlements

    @applyMarketDataEntitlements.setter
    def applyMarketDataEntitlements(self, value: bool):
        self.__applyMarketDataEntitlements = value
        self._property_changed('applyMarketDataEntitlements')        

    @property
    def uploadDataPolicy(self) -> str:
        """Policy governing uploads."""
        return self.__uploadDataPolicy

    @uploadDataPolicy.setter
    def uploadDataPolicy(self, value: str):
        self.__uploadDataPolicy = value
        self._property_changed('uploadDataPolicy')        

    @property
    def identifierMapperName(self) -> str:
        """Identifier mapper associated with dataset."""
        return self.__identifierMapperName

    @identifierMapperName.setter
    def identifierMapperName(self, value: str):
        self.__identifierMapperName = value
        self._property_changed('identifierMapperName')        

    @property
    def identifierUpdaterName(self) -> str:
        """Identifier updater associated with dataset."""
        return 'REPORT_IDENTIFIER_UPDATER'        

    @property
    def logicalDb(self) -> str:
        """Database where contents are (to be) stored."""
        return self.__logicalDb

    @logicalDb.setter
    def logicalDb(self, value: str):
        self.__logicalDb = value
        self._property_changed('logicalDb')        

    @property
    def symbolStrategy(self) -> str:
        """Method for looking up database table name."""
        return self.__symbolStrategy

    @symbolStrategy.setter
    def symbolStrategy(self, value: str):
        self.__symbolStrategy = value
        self._property_changed('symbolStrategy')        

    @property
    def constantSymbols(self) -> Tuple[str, ...]:
        return self.__constantSymbols

    @constantSymbols.setter
    def constantSymbols(self, value: Tuple[str, ...]):
        self.__constantSymbols = value
        self._property_changed('constantSymbols')        

    @property
    def underlyingDataSetId(self) -> str:
        """Dataset on which this (virtual) dataset is based."""
        return self.__underlyingDataSetId

    @underlyingDataSetId.setter
    def underlyingDataSetId(self, value: str):
        self.__underlyingDataSetId = value
        self._property_changed('underlyingDataSetId')        

    @property
    def immutable(self) -> bool:
        """Whether dataset is immutable (i.e. not writable through data service)."""
        return self.__immutable

    @immutable.setter
    def immutable(self, value: bool):
        self.__immutable = value
        self._property_changed('immutable')        

    @property
    def includeInCatalog(self) -> bool:
        """Whether dataset should be in the catalog."""
        return self.__includeInCatalog

    @includeInCatalog.setter
    def includeInCatalog(self, value: bool):
        self.__includeInCatalog = value
        self._property_changed('includeInCatalog')        

    @property
    def overrideQueryColumnIds(self) -> Tuple[str, ...]:
        """Explicit set of database columns to query for, regardless of fields specified in request."""
        return self.__overrideQueryColumnIds

    @overrideQueryColumnIds.setter
    def overrideQueryColumnIds(self, value: Tuple[str, ...]):
        self.__overrideQueryColumnIds = value
        self._property_changed('overrideQueryColumnIds')        

    @property
    def plot(self) -> bool:
        """Whether dataset is intended for use in Plottool."""
        return self.__plot

    @plot.setter
    def plot(self, value: bool):
        self.__plot = value
        self._property_changed('plot')        

    @property
    def coverageEnabled(self) -> bool:
        """Whether coverage requests are available for the DataSet"""
        return self.__coverageEnabled

    @coverageEnabled.setter
    def coverageEnabled(self, value: bool):
        self.__coverageEnabled = value
        self._property_changed('coverageEnabled')        


class MarketDataMapping(Base):
               
    def __init__(self, assetClass: Union[AssetClass, str] = None, queryType: str = None, description: str = None, scale: float = None, frequency: Union[MarketDataFrequency, str] = None, measures: Tuple[Union[MarketDataMeasure, str], ...] = None, dataSet: str = None, vendor: Union[MarketDataVendor, str] = None, fields: Tuple[MarketDataField, ...] = None, rank: float = None, filteredFields: Tuple[MarketDataFilteredField, ...] = None, assetTypes: Tuple[Union[AssetType, str], ...] = None, entityType: Union[MeasureEntityType, str] = None, backtestEntity: MeasureBacktest = None, kpiEntity: MeasureKpi = None):
        super().__init__()
        self.__assetClass = assetClass if isinstance(assetClass, AssetClass) else get_enum_value(AssetClass, assetClass)
        self.__queryType = queryType
        self.__description = description
        self.__scale = scale
        self.__frequency = frequency if isinstance(frequency, MarketDataFrequency) else get_enum_value(MarketDataFrequency, frequency)
        self.__measures = measures
        self.__dataSet = dataSet
        self.__vendor = vendor if isinstance(vendor, MarketDataVendor) else get_enum_value(MarketDataVendor, vendor)
        self.__fields = fields
        self.__rank = rank
        self.__filteredFields = filteredFields
        self.__assetTypes = assetTypes
        self.__entityType = entityType if isinstance(entityType, MeasureEntityType) else get_enum_value(MeasureEntityType, entityType)
        self.__backtestEntity = backtestEntity
        self.__kpiEntity = kpiEntity

    @property
    def assetClass(self) -> Union[AssetClass, str]:
        """Asset class that is applicable for mapping."""
        return self.__assetClass

    @assetClass.setter
    def assetClass(self, value: Union[AssetClass, str]):
        self.__assetClass = value if isinstance(value, AssetClass) else get_enum_value(AssetClass, value)
        self._property_changed('assetClass')        

    @property
    def queryType(self) -> str:
        """Market data query type."""
        return self.__queryType

    @queryType.setter
    def queryType(self, value: str):
        self.__queryType = value
        self._property_changed('queryType')        

    @property
    def description(self) -> str:
        """Query type description"""
        return self.__description

    @description.setter
    def description(self, value: str):
        self.__description = value
        self._property_changed('description')        

    @property
    def scale(self) -> float:
        """Scale multiplier for time series"""
        return self.__scale

    @scale.setter
    def scale(self, value: float):
        self.__scale = value
        self._property_changed('scale')        

    @property
    def frequency(self) -> Union[MarketDataFrequency, str]:
        return self.__frequency

    @frequency.setter
    def frequency(self, value: Union[MarketDataFrequency, str]):
        self.__frequency = value if isinstance(value, MarketDataFrequency) else get_enum_value(MarketDataFrequency, value)
        self._property_changed('frequency')        

    @property
    def measures(self) -> Tuple[Union[MarketDataMeasure, str], ...]:
        return self.__measures

    @measures.setter
    def measures(self, value: Tuple[Union[MarketDataMeasure, str], ...]):
        self.__measures = value
        self._property_changed('measures')        

    @property
    def dataSet(self) -> str:
        """Marquee unique identifier"""
        return self.__dataSet

    @dataSet.setter
    def dataSet(self, value: str):
        self.__dataSet = value
        self._property_changed('dataSet')        

    @property
    def vendor(self) -> Union[MarketDataVendor, str]:
        return self.__vendor

    @vendor.setter
    def vendor(self, value: Union[MarketDataVendor, str]):
        self.__vendor = value if isinstance(value, MarketDataVendor) else get_enum_value(MarketDataVendor, value)
        self._property_changed('vendor')        

    @property
    def fields(self) -> Tuple[MarketDataField, ...]:
        return self.__fields

    @fields.setter
    def fields(self, value: Tuple[MarketDataField, ...]):
        self.__fields = value
        self._property_changed('fields')        

    @property
    def rank(self) -> float:
        return self.__rank

    @rank.setter
    def rank(self, value: float):
        self.__rank = value
        self._property_changed('rank')        

    @property
    def filteredFields(self) -> Tuple[MarketDataFilteredField, ...]:
        return self.__filteredFields

    @filteredFields.setter
    def filteredFields(self, value: Tuple[MarketDataFilteredField, ...]):
        self.__filteredFields = value
        self._property_changed('filteredFields')        

    @property
    def assetTypes(self) -> Tuple[Union[AssetType, str], ...]:
        """Asset type differentiates the product categorization or contract type"""
        return self.__assetTypes

    @assetTypes.setter
    def assetTypes(self, value: Tuple[Union[AssetType, str], ...]):
        self.__assetTypes = value
        self._property_changed('assetTypes')        

    @property
    def entityType(self) -> Union[MeasureEntityType, str]:
        """Entity type associated with a measure."""
        return self.__entityType

    @entityType.setter
    def entityType(self, value: Union[MeasureEntityType, str]):
        self.__entityType = value if isinstance(value, MeasureEntityType) else get_enum_value(MeasureEntityType, value)
        self._property_changed('entityType')        

    @property
    def backtestEntity(self) -> MeasureBacktest:
        """Describes backtests that should be associated with a measure."""
        return self.__backtestEntity

    @backtestEntity.setter
    def backtestEntity(self, value: MeasureBacktest):
        self.__backtestEntity = value
        self._property_changed('backtestEntity')        

    @property
    def kpiEntity(self) -> MeasureKpi:
        """Describes KPIs that should be associated with a measure."""
        return self.__kpiEntity

    @kpiEntity.setter
    def kpiEntity(self, value: MeasureKpi):
        self.__kpiEntity = value
        self._property_changed('kpiEntity')        


class ProcessorEntity(Base):
        
    """Query processors for dataset."""
       
    def __init__(self, filters: Tuple[str, ...] = None, parsers: Tuple[ParserEntity, ...] = None, deduplicate: Tuple[str, ...] = None):
        super().__init__()
        self.__filters = filters
        self.__parsers = parsers
        self.__deduplicate = deduplicate

    @property
    def filters(self) -> Tuple[str, ...]:
        """List of filter processors."""
        return self.__filters

    @filters.setter
    def filters(self, value: Tuple[str, ...]):
        self.__filters = value
        self._property_changed('filters')        

    @property
    def parsers(self) -> Tuple[ParserEntity, ...]:
        """List of parser processors."""
        return self.__parsers

    @parsers.setter
    def parsers(self, value: Tuple[ParserEntity, ...]):
        self.__parsers = value
        self._property_changed('parsers')        

    @property
    def deduplicate(self) -> Tuple[str, ...]:
        """Columns on which a deduplication processor should be run."""
        return self.__deduplicate

    @deduplicate.setter
    def deduplicate(self, value: Tuple[str, ...]):
        self.__deduplicate = value
        self._property_changed('deduplicate')        


class EntityFilter(Base):
        
    """Filter on entities."""
       
    def __init__(self, operator: str = None, simpleFilters: Tuple[DataFilter, ...] = None, complexFilters: Tuple[ComplexFilter, ...] = None):
        super().__init__()
        self.__operator = operator
        self.__simpleFilters = simpleFilters
        self.__complexFilters = complexFilters

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, value: str):
        self.__operator = value
        self._property_changed('operator')        

    @property
    def simpleFilters(self) -> Tuple[DataFilter, ...]:
        """Filter on specified field."""
        return self.__simpleFilters

    @simpleFilters.setter
    def simpleFilters(self, value: Tuple[DataFilter, ...]):
        self.__simpleFilters = value
        self._property_changed('simpleFilters')        

    @property
    def complexFilters(self) -> Tuple[ComplexFilter, ...]:
        """A compound filter for data requests."""
        return self.__complexFilters

    @complexFilters.setter
    def complexFilters(self, value: Tuple[ComplexFilter, ...]):
        self.__complexFilters = value
        self._property_changed('complexFilters')        


class FieldFilterMap(Base):
               
    def __init__(self, **kwargs):
        super().__init__()
        self.__queueClockTimeLabel = kwargs.get('queueClockTimeLabel')
        self.__marketPnl = kwargs.get('marketPnl')
        self.__year = kwargs.get('year')
        self.__sustainAsiaExJapan = kwargs.get('sustainAsiaExJapan')
        self.__investmentRate = kwargs.get('investmentRate')
        self.__assetClassificationsGicsSubIndustry = kwargs.get('assetClassificationsGicsSubIndustry')
        self.__mdapiClass = kwargs.get('mdapiClass')
        self.__bidUnadjusted = kwargs.get('bidUnadjusted')
        self.__economicTermsHash = kwargs.get('economicTermsHash')
        self.__neighbourAssetId = kwargs.get('neighbourAssetId')
        self.__simonIntlAssetTags = kwargs.get('simonIntlAssetTags')
        self.__path = kwargs.get('path')
        self.__availableInventory = kwargs.get('availableInventory')
        self.__clientContact = kwargs.get('clientContact')
        self.__est1DayCompletePct = kwargs.get('est1DayCompletePct')
        self.__rank = kwargs.get('rank')
        self.__dataSetCategory = kwargs.get('dataSetCategory')
        self.__createdById = kwargs.get('createdById')
        self.__vehicleType = kwargs.get('vehicleType')
        self.__dailyRisk = kwargs.get('dailyRisk')
        self.__bosInBpsLabel = kwargs.get('bosInBpsLabel')
        self.__energy = kwargs.get('energy')
        self.__marketDataType = kwargs.get('marketDataType')
        self.__sentimentScore = kwargs.get('sentimentScore')
        self.__bosInBps = kwargs.get('bosInBps')
        self.__pointClass = kwargs.get('pointClass')
        self.__fxSpot = kwargs.get('fxSpot')
        self.__bidLow = kwargs.get('bidLow')
        self.__valuePrevious = kwargs.get('valuePrevious')
        self.__fairVarianceVolatility = kwargs.get('fairVarianceVolatility')
        self.__avgTradeRate = kwargs.get('avgTradeRate')
        self.__shortLevel = kwargs.get('shortLevel')
        self.__hedgeVolatility = kwargs.get('hedgeVolatility')
        self.__version = kwargs.get('version')
        self.__tags = kwargs.get('tags')
        self.__underlyingAssetId = kwargs.get('underlyingAssetId')
        self.__clientExposure = kwargs.get('clientExposure')
        self.__correlation = kwargs.get('correlation')
        self.__exposure = kwargs.get('exposure')
        self.__gsSustainSubSector = kwargs.get('gsSustainSubSector')
        self.__domain = kwargs.get('domain')
        self.__marketDataAsset = kwargs.get('marketDataAsset')
        self.__forwardTenor = kwargs.get('forwardTenor')
        self.__unadjustedHigh = kwargs.get('unadjustedHigh')
        self.__sourceImportance = kwargs.get('sourceImportance')
        self.__eid = kwargs.get('eid')
        self.__jsn = kwargs.get('jsn')
        self.__relativeReturnQtd = kwargs.get('relativeReturnQtd')
        self.__displayName = kwargs.get('displayName')
        self.__minutesToTrade100Pct = kwargs.get('minutesToTrade100Pct')
        self.__marketModelId = kwargs.get('marketModelId')
        self.__quoteType = kwargs.get('quoteType')
        self.__realizedCorrelation = kwargs.get('realizedCorrelation')
        self.__tenor = kwargs.get('tenor')
        self.__esPolicyPercentile = kwargs.get('esPolicyPercentile')
        self.__atmFwdRate = kwargs.get('atmFwdRate')
        self.__tcmCostParticipationRate75Pct = kwargs.get('tcmCostParticipationRate75Pct')
        self.__close = kwargs.get('close')
        self.__tcmCostParticipationRate100Pct = kwargs.get('tcmCostParticipationRate100Pct')
        self.__disclaimer = kwargs.get('disclaimer')
        self.__measureIdx = kwargs.get('measureIdx')
        self.__a = kwargs.get('a')
        self.__b = kwargs.get('b')
        self.__loanFee = kwargs.get('loanFee')
        self.__c = kwargs.get('c')
        self.__equityVega = kwargs.get('equityVega')
        self.__lenderPayment = kwargs.get('lenderPayment')
        self.__deploymentVersion = kwargs.get('deploymentVersion')
        self.__fiveDayMove = kwargs.get('fiveDayMove')
        self.__borrower = kwargs.get('borrower')
        self.__valueFormat = kwargs.get('valueFormat')
        self.__performanceContribution = kwargs.get('performanceContribution')
        self.__targetNotional = kwargs.get('targetNotional')
        self.__fillLegId = kwargs.get('fillLegId')
        self.__delisted = kwargs.get('delisted')
        self.__rationale = kwargs.get('rationale')
        self.__regionalFocus = kwargs.get('regionalFocus')
        self.__volumePrimary = kwargs.get('volumePrimary')
        self.__series = kwargs.get('series')
        self.__simonId = kwargs.get('simonId')
        self.__newIdeasQtd = kwargs.get('newIdeasQtd')
        self.__congestion = kwargs.get('congestion')
        self.__adjustedAskPrice = kwargs.get('adjustedAskPrice')
        self.__quarter = kwargs.get('quarter')
        self.__factorUniverse = kwargs.get('factorUniverse')
        self.__eventCategory = kwargs.get('eventCategory')
        self.__impliedNormalVolatility = kwargs.get('impliedNormalVolatility')
        self.__unadjustedOpen = kwargs.get('unadjustedOpen')
        self.__arrivalRt = kwargs.get('arrivalRt')
        self.__criticality = kwargs.get('criticality')
        self.__transactionCost = kwargs.get('transactionCost')
        self.__servicingCostShortPnl = kwargs.get('servicingCostShortPnl')
        self.__bidAskSpread = kwargs.get('bidAskSpread')
        self.__optionType = kwargs.get('optionType')
        self.__tcmCostHorizon3Hour = kwargs.get('tcmCostHorizon3Hour')
        self.__clusterDescription = kwargs.get('clusterDescription')
        self.__creditLimit = kwargs.get('creditLimit')
        self.__positionAmount = kwargs.get('positionAmount')
        self.__numberOfPositions = kwargs.get('numberOfPositions')
        self.__windSpeed = kwargs.get('windSpeed')
        self.__openUnadjusted = kwargs.get('openUnadjusted')
        self.__maRank = kwargs.get('maRank')
        self.__askPrice = kwargs.get('askPrice')
        self.__eventId = kwargs.get('eventId')
        self.__borrowerId = kwargs.get('borrowerId')
        self.__dataProduct = kwargs.get('dataProduct')
        self.__sectors = kwargs.get('sectors')
        self.__mqSymbol = kwargs.get('mqSymbol')
        self.__annualizedTrackingError = kwargs.get('annualizedTrackingError')
        self.__volSwap = kwargs.get('volSwap')
        self.__annualizedRisk = kwargs.get('annualizedRisk')
        self.__bmPrimeId = kwargs.get('bmPrimeId')
        self.__corporateAction = kwargs.get('corporateAction')
        self.__conviction = kwargs.get('conviction')
        self.__grossExposure = kwargs.get('grossExposure')
        self.__benchmarkMaturity = kwargs.get('benchmarkMaturity')
        self.__gRegionalScore = kwargs.get('gRegionalScore')
        self.__volumeComposite = kwargs.get('volumeComposite')
        self.__volume = kwargs.get('volume')
        self.__factorId = kwargs.get('factorId')
        self.__hardToBorrow = kwargs.get('hardToBorrow')
        self.__adv = kwargs.get('adv')
        self.__stsFxCurrency = kwargs.get('stsFxCurrency')
        self.__wpk = kwargs.get('wpk')
        self.__shortConvictionMedium = kwargs.get('shortConvictionMedium')
        self.__bidChange = kwargs.get('bidChange')
        self.__exchange = kwargs.get('exchange')
        self.__expiration = kwargs.get('expiration')
        self.__tradePrice = kwargs.get('tradePrice')
        self.__esPolicyScore = kwargs.get('esPolicyScore')
        self.__loanId = kwargs.get('loanId')
        self.__primeIdNumeric = kwargs.get('primeIdNumeric')
        self.__cid = kwargs.get('cid')
        self.__onboarded = kwargs.get('onboarded')
        self.__liquidityScore = kwargs.get('liquidityScore')
        self.__importance = kwargs.get('importance')
        self.__sourceDateSpan = kwargs.get('sourceDateSpan')
        self.__assetClassificationsGicsSector = kwargs.get('assetClassificationsGicsSector')
        self.__underlyingDataSetId = kwargs.get('underlyingDataSetId')
        self.__stsAssetName = kwargs.get('stsAssetName')
        self.__closeUnadjusted = kwargs.get('closeUnadjusted')
        self.__valueUnit = kwargs.get('valueUnit')
        self.__bidHigh = kwargs.get('bidHigh')
        self.__adjustedLowPrice = kwargs.get('adjustedLowPrice')
        self.__netExposureClassification = kwargs.get('netExposureClassification')
        self.__longConvictionLarge = kwargs.get('longConvictionLarge')
        self.__fairVariance = kwargs.get('fairVariance')
        self.__hitRateWtd = kwargs.get('hitRateWtd')
        self.__oad = kwargs.get('oad')
        self.__bosInBpsDescription = kwargs.get('bosInBpsDescription')
        self.__lowPrice = kwargs.get('lowPrice')
        self.__realizedVolatility = kwargs.get('realizedVolatility')
        self.__rate = kwargs.get('rate')
        self.__adv22DayPct = kwargs.get('adv22DayPct')
        self.__alpha = kwargs.get('alpha')
        self.__client = kwargs.get('client')
        self.__cloneParentId = kwargs.get('cloneParentId')
        self.__company = kwargs.get('company')
        self.__convictionList = kwargs.get('convictionList')
        self.__priceRangeInTicksLabel = kwargs.get('priceRangeInTicksLabel')
        self.__ticker = kwargs.get('ticker')
        self.__inRiskModel = kwargs.get('inRiskModel')
        self.__tcmCostHorizon1Day = kwargs.get('tcmCostHorizon1Day')
        self.__servicingCostLongPnl = kwargs.get('servicingCostLongPnl')
        self.__stsRatesCountry = kwargs.get('stsRatesCountry')
        self.__meetingNumber = kwargs.get('meetingNumber')
        self.__exchangeId = kwargs.get('exchangeId')
        self.__horizon = kwargs.get('horizon')
        self.__midGspread = kwargs.get('midGspread')
        self.__tcmCostHorizon20Day = kwargs.get('tcmCostHorizon20Day')
        self.__longLevel = kwargs.get('longLevel')
        self.__sourceValueForecast = kwargs.get('sourceValueForecast')
        self.__shortConvictionLarge = kwargs.get('shortConvictionLarge')
        self.__realm = kwargs.get('realm')
        self.__bid = kwargs.get('bid')
        self.__dataDescription = kwargs.get('dataDescription')
        self.__counterPartyStatus = kwargs.get('counterPartyStatus')
        self.__composite22DayAdv = kwargs.get('composite22DayAdv')
        self.__dollarExcessReturn = kwargs.get('dollarExcessReturn')
        self.__gsn = kwargs.get('gsn')
        self.__isAggressive = kwargs.get('isAggressive')
        self.__orderId = kwargs.get('orderId')
        self.__gss = kwargs.get('gss')
        self.__percentOfMediandv1m = kwargs.get('percentOfMediandv1m')
        self.__lendables = kwargs.get('lendables')
        self.__assetClass = kwargs.get('assetClass')
        self.__gsideid = kwargs.get('gsideid')
        self.__bosInTicksLabel = kwargs.get('bosInTicksLabel')
        self.__ric = kwargs.get('ric')
        self.__positionSourceId = kwargs.get('positionSourceId')
        self.__division = kwargs.get('division')
        self.__marketCapUSD = kwargs.get('marketCapUSD')
        self.__gsSustainRegion = kwargs.get('gsSustainRegion')
        self.__deploymentId = kwargs.get('deploymentId')
        self.__highPrice = kwargs.get('highPrice')
        self.__loanStatus = kwargs.get('loanStatus')
        self.__shortWeight = kwargs.get('shortWeight')
        self.__absoluteShares = kwargs.get('absoluteShares')
        self.__action = kwargs.get('action')
        self.__model = kwargs.get('model')
        self.__id = kwargs.get('id')
        self.__arrivalHaircutVwapNormalized = kwargs.get('arrivalHaircutVwapNormalized')
        self.__priceComponent = kwargs.get('priceComponent')
        self.__queueClockTimeDescription = kwargs.get('queueClockTimeDescription')
        self.__loanRebate = kwargs.get('loanRebate')
        self.__period = kwargs.get('period')
        self.__indexCreateSource = kwargs.get('indexCreateSource')
        self.__fiscalQuarter = kwargs.get('fiscalQuarter')
        self.__deltaStrike = kwargs.get('deltaStrike')
        self.__marketImpact = kwargs.get('marketImpact')
        self.__eventType = kwargs.get('eventType')
        self.__assetCountLong = kwargs.get('assetCountLong')
        self.__valueActual = kwargs.get('valueActual')
        self.__bcid = kwargs.get('bcid')
        self.__collateralCurrency = kwargs.get('collateralCurrency')
        self.__originalCountry = kwargs.get('originalCountry')
        self.__touchLiquidityScore = kwargs.get('touchLiquidityScore')
        self.__field = kwargs.get('field')
        self.__factorCategoryId = kwargs.get('factorCategoryId')
        self.__spot = kwargs.get('spot')
        self.__expectedCompletionDate = kwargs.get('expectedCompletionDate')
        self.__loanValue = kwargs.get('loanValue')
        self.__tradingRestriction = kwargs.get('tradingRestriction')
        self.__skew = kwargs.get('skew')
        self.__status = kwargs.get('status')
        self.__sustainEmergingMarkets = kwargs.get('sustainEmergingMarkets')
        self.__totalReturnPrice = kwargs.get('totalReturnPrice')
        self.__city = kwargs.get('city')
        self.__totalPrice = kwargs.get('totalPrice')
        self.__eventSource = kwargs.get('eventSource')
        self.__qisPermNo = kwargs.get('qisPermNo')
        self.__hitRateYtd = kwargs.get('hitRateYtd')
        self.__valid = kwargs.get('valid')
        self.__stsCommodity = kwargs.get('stsCommodity')
        self.__stsCommoditySector = kwargs.get('stsCommoditySector')
        self.__exceptionStatus = kwargs.get('exceptionStatus')
        self.__salesCoverage = kwargs.get('salesCoverage')
        self.__shortExposure = kwargs.get('shortExposure')
        self.__esScore = kwargs.get('esScore')
        self.__tcmCostParticipationRate10Pct = kwargs.get('tcmCostParticipationRate10Pct')
        self.__eventTime = kwargs.get('eventTime')
        self.__positionSourceName = kwargs.get('positionSourceName')
        self.__priceRangeInTicks = kwargs.get('priceRangeInTicks')
        self.__arrivalHaircutVwap = kwargs.get('arrivalHaircutVwap')
        self.__interestRate = kwargs.get('interestRate')
        self.__executionDays = kwargs.get('executionDays')
        self.__pctChange = kwargs.get('pctChange')
        self.__side = kwargs.get('side')
        self.__numberOfRolls = kwargs.get('numberOfRolls')
        self.__agentLenderFee = kwargs.get('agentLenderFee')
        self.__complianceRestrictedStatus = kwargs.get('complianceRestrictedStatus')
        self.__forward = kwargs.get('forward')
        self.__borrowFee = kwargs.get('borrowFee')
        self.__strike = kwargs.get('strike')
        self.__loanSpread = kwargs.get('loanSpread')
        self.__tcmCostHorizon12Hour = kwargs.get('tcmCostHorizon12Hour')
        self.__dewPoint = kwargs.get('dewPoint')
        self.__researchCommission = kwargs.get('researchCommission')
        self.__bbid = kwargs.get('bbid')
        self.__assetClassificationsRiskCountryCode = kwargs.get('assetClassificationsRiskCountryCode')
        self.__eventStatus = kwargs.get('eventStatus')
        self.__return = kwargs.get('return_')
        self.__maxTemperature = kwargs.get('maxTemperature')
        self.__acquirerShareholderMeetingDate = kwargs.get('acquirerShareholderMeetingDate')
        self.__arrivalMidNormalized = kwargs.get('arrivalMidNormalized')
        self.__rating = kwargs.get('rating')
        self.__volatility = kwargs.get('volatility')
        self.__arrivalRtNormalized = kwargs.get('arrivalRtNormalized')
        self.__performanceFee = kwargs.get('performanceFee')
        self.__reportType = kwargs.get('reportType')
        self.__sourceURL = kwargs.get('sourceURL')
        self.__estimatedReturn = kwargs.get('estimatedReturn')
        self.__underlyingAssetIds = kwargs.get('underlyingAssetIds')
        self.__high = kwargs.get('high')
        self.__sourceLastUpdate = kwargs.get('sourceLastUpdate')
        self.__queueInLotsLabel = kwargs.get('queueInLotsLabel')
        self.__adv10DayPct = kwargs.get('adv10DayPct')
        self.__longConvictionMedium = kwargs.get('longConvictionMedium')
        self.__eventName = kwargs.get('eventName')
        self.__annualRisk = kwargs.get('annualRisk')
        self.__eti = kwargs.get('eti')
        self.__dailyTrackingError = kwargs.get('dailyTrackingError')
        self.__unadjustedBid = kwargs.get('unadjustedBid')
        self.__gsdeer = kwargs.get('gsdeer')
        self.__gRegionalPercentile = kwargs.get('gRegionalPercentile')
        self.__marketBuffer = kwargs.get('marketBuffer')
        self.__marketCap = kwargs.get('marketCap')
        self.__oeId = kwargs.get('oeId')
        self.__clusterRegion = kwargs.get('clusterRegion')
        self.__bbidEquivalent = kwargs.get('bbidEquivalent')
        self.__prevCloseAsk = kwargs.get('prevCloseAsk')
        self.__level = kwargs.get('level')
        self.__valoren = kwargs.get('valoren')
        self.__esMomentumScore = kwargs.get('esMomentumScore')
        self.__pressure = kwargs.get('pressure')
        self.__shortDescription = kwargs.get('shortDescription')
        self.__basis = kwargs.get('basis')
        self.__netWeight = kwargs.get('netWeight')
        self.__hedgeId = kwargs.get('hedgeId')
        self.__portfolioManagers = kwargs.get('portfolioManagers')
        self.__assetParametersCommoditySector = kwargs.get('assetParametersCommoditySector')
        self.__bosInTicks = kwargs.get('bosInTicks')
        self.__tcmCostHorizon8Day = kwargs.get('tcmCostHorizon8Day')
        self.__supraStrategy = kwargs.get('supraStrategy')
        self.__marketBufferThreshold = kwargs.get('marketBufferThreshold')
        self.__adv5DayPct = kwargs.get('adv5DayPct')
        self.__factorSource = kwargs.get('factorSource')
        self.__leverage = kwargs.get('leverage')
        self.__submitter = kwargs.get('submitter')
        self.__notional = kwargs.get('notional')
        self.__esDisclosurePercentage = kwargs.get('esDisclosurePercentage')
        self.__investmentIncome = kwargs.get('investmentIncome')
        self.__clientShortName = kwargs.get('clientShortName')
        self.__fwdPoints = kwargs.get('fwdPoints')
        self.__groupCategory = kwargs.get('groupCategory')
        self.__kpiId = kwargs.get('kpiId')
        self.__relativeReturnWtd = kwargs.get('relativeReturnWtd')
        self.__bidPlusAsk = kwargs.get('bidPlusAsk')
        self.__borrowCost = kwargs.get('borrowCost')
        self.__assetClassificationsRiskCountryName = kwargs.get('assetClassificationsRiskCountryName')
        self.__total = kwargs.get('total')
        self.__riskModel = kwargs.get('riskModel')
        self.__assetId = kwargs.get('assetId')
        self.__averageImpliedVolatility = kwargs.get('averageImpliedVolatility')
        self.__fairValue = kwargs.get('fairValue')
        self.__adjustedHighPrice = kwargs.get('adjustedHighPrice')
        self.__beta = kwargs.get('beta')
        self.__direction = kwargs.get('direction')
        self.__valueForecast = kwargs.get('valueForecast')
        self.__longExposure = kwargs.get('longExposure')
        self.__positionSourceType = kwargs.get('positionSourceType')
        self.__tcmCostParticipationRate20Pct = kwargs.get('tcmCostParticipationRate20Pct')
        self.__adjustedClosePrice = kwargs.get('adjustedClosePrice')
        self.__cross = kwargs.get('cross')
        self.__lmsId = kwargs.get('lmsId')
        self.__rebateRate = kwargs.get('rebateRate')
        self.__ideaStatus = kwargs.get('ideaStatus')
        self.__participationRate = kwargs.get('participationRate')
        self.__obfr = kwargs.get('obfr')
        self.__fxForecast = kwargs.get('fxForecast')
        self.__fixingTimeLabel = kwargs.get('fixingTimeLabel')
        self.__implementationId = kwargs.get('implementationId')
        self.__fillId = kwargs.get('fillId')
        self.__excessReturns = kwargs.get('excessReturns')
        self.__esMomentumPercentile = kwargs.get('esMomentumPercentile')
        self.__dollarReturn = kwargs.get('dollarReturn')
        self.__esNumericScore = kwargs.get('esNumericScore')
        self.__lenderIncomeAdjustment = kwargs.get('lenderIncomeAdjustment')
        self.__inBenchmark = kwargs.get('inBenchmark')
        self.__strategy = kwargs.get('strategy')
        self.__positionType = kwargs.get('positionType')
        self.__lenderIncome = kwargs.get('lenderIncome')
        self.__shortInterest = kwargs.get('shortInterest')
        self.__referencePeriod = kwargs.get('referencePeriod')
        self.__adjustedVolume = kwargs.get('adjustedVolume')
        self.__queueInLotsDescription = kwargs.get('queueInLotsDescription')
        self.__pbClientId = kwargs.get('pbClientId')
        self.__ownerId = kwargs.get('ownerId')
        self.__secDB = kwargs.get('secDB')
        self.__composite10DayAdv = kwargs.get('composite10DayAdv')
        self.__objective = kwargs.get('objective')
        self.__bpeQualityStars = kwargs.get('bpeQualityStars')
        self.__navPrice = kwargs.get('navPrice')
        self.__ideaActivityType = kwargs.get('ideaActivityType')
        self.__precipitation = kwargs.get('precipitation')
        self.__ideaSource = kwargs.get('ideaSource')
        self.__hedgeNotional = kwargs.get('hedgeNotional')
        self.__askLow = kwargs.get('askLow')
        self.__unadjustedAsk = kwargs.get('unadjustedAsk')
        self.__betaAdjustedNetExposure = kwargs.get('betaAdjustedNetExposure')
        self.__expiry = kwargs.get('expiry')
        self.__tradingPnl = kwargs.get('tradingPnl')
        self.__strikePercentage = kwargs.get('strikePercentage')
        self.__excessReturnPrice = kwargs.get('excessReturnPrice')
        self.__givenPlusPaid = kwargs.get('givenPlusPaid')
        self.__shortConvictionSmall = kwargs.get('shortConvictionSmall')
        self.__prevCloseBid = kwargs.get('prevCloseBid')
        self.__fxPnl = kwargs.get('fxPnl')
        self.__forecast = kwargs.get('forecast')
        self.__tcmCostHorizon16Day = kwargs.get('tcmCostHorizon16Day')
        self.__pnl = kwargs.get('pnl')
        self.__assetClassificationsGicsIndustryGroup = kwargs.get('assetClassificationsGicsIndustryGroup')
        self.__unadjustedClose = kwargs.get('unadjustedClose')
        self.__tcmCostHorizon4Day = kwargs.get('tcmCostHorizon4Day')
        self.__assetClassificationsIsPrimary = kwargs.get('assetClassificationsIsPrimary')
        self.__styles = kwargs.get('styles')
        self.__lendingSecId = kwargs.get('lendingSecId')
        self.__shortName = kwargs.get('shortName')
        self.__equityTheta = kwargs.get('equityTheta')
        self.__averageFillPrice = kwargs.get('averageFillPrice')
        self.__snowfall = kwargs.get('snowfall')
        self.__mic = kwargs.get('mic')
        self.__bidGspread = kwargs.get('bidGspread')
        self.__openPrice = kwargs.get('openPrice')
        self.__mid = kwargs.get('mid')
        self.__autoExecState = kwargs.get('autoExecState')
        self.__depthSpreadScore = kwargs.get('depthSpreadScore')
        self.__relativeReturnYtd = kwargs.get('relativeReturnYtd')
        self.__long = kwargs.get('long')
        self.__subAccount = kwargs.get('subAccount')
        self.__fairVolatility = kwargs.get('fairVolatility')
        self.__dollarCross = kwargs.get('dollarCross')
        self.__portfolioType = kwargs.get('portfolioType')
        self.__longWeight = kwargs.get('longWeight')
        self.__calculationTime = kwargs.get('calculationTime')
        self.__vendor = kwargs.get('vendor')
        self.__currency = kwargs.get('currency')
        self.__realTimeRestrictionStatus = kwargs.get('realTimeRestrictionStatus')
        self.__averageRealizedVariance = kwargs.get('averageRealizedVariance')
        self.__clusterClass = kwargs.get('clusterClass')
        self.__financialReturnsScore = kwargs.get('financialReturnsScore')
        self.__netChange = kwargs.get('netChange')
        self.__nonSymbolDimensions = kwargs.get('nonSymbolDimensions')
        self.__queueingTime = kwargs.get('queueingTime')
        self.__bidSize = kwargs.get('bidSize')
        self.__swapType = kwargs.get('swapType')
        self.__arrivalMid = kwargs.get('arrivalMid')
        self.__assetParametersExchangeCurrency = kwargs.get('assetParametersExchangeCurrency')
        self.__unexplained = kwargs.get('unexplained')
        self.__assetClassificationsCountryName = kwargs.get('assetClassificationsCountryName')
        self.__metric = kwargs.get('metric')
        self.__newIdeasYtd = kwargs.get('newIdeasYtd')
        self.__managementFee = kwargs.get('managementFee')
        self.__ask = kwargs.get('ask')
        self.__impliedLognormalVolatility = kwargs.get('impliedLognormalVolatility')
        self.__closePrice = kwargs.get('closePrice')
        self.__open = kwargs.get('open')
        self.__sourceId = kwargs.get('sourceId')
        self.__country = kwargs.get('country')
        self.__cusip = kwargs.get('cusip')
        self.__touchSpreadScore = kwargs.get('touchSpreadScore')
        self.__absoluteStrike = kwargs.get('absoluteStrike')
        self.__netExposure = kwargs.get('netExposure')
        self.__source = kwargs.get('source')
        self.__assetClassificationsCountryCode = kwargs.get('assetClassificationsCountryCode')
        self.__frequency = kwargs.get('frequency')
        self.__activityId = kwargs.get('activityId')
        self.__estimatedImpact = kwargs.get('estimatedImpact')
        self.__dataSetSubCategory = kwargs.get('dataSetSubCategory')
        self.__loanSpreadBucket = kwargs.get('loanSpreadBucket')
        self.__assetParametersPricingLocation = kwargs.get('assetParametersPricingLocation')
        self.__eventDescription = kwargs.get('eventDescription')
        self.__strikeReference = kwargs.get('strikeReference')
        self.__details = kwargs.get('details')
        self.__assetCount = kwargs.get('assetCount')
        self.__quantityBucket = kwargs.get('quantityBucket')
        self.__oeName = kwargs.get('oeName')
        self.__given = kwargs.get('given')
        self.__absoluteValue = kwargs.get('absoluteValue')
        self.__delistingDate = kwargs.get('delistingDate')
        self.__longTenor = kwargs.get('longTenor')
        self.__mctr = kwargs.get('mctr')
        self.__weight = kwargs.get('weight')
        self.__historicalClose = kwargs.get('historicalClose')
        self.__assetCountPriced = kwargs.get('assetCountPriced')
        self.__marketDataPoint = kwargs.get('marketDataPoint')
        self.__ideaId = kwargs.get('ideaId')
        self.__commentStatus = kwargs.get('commentStatus')
        self.__marginalCost = kwargs.get('marginalCost')
        self.__absoluteWeight = kwargs.get('absoluteWeight')
        self.__measure = kwargs.get('measure')
        self.__clientWeight = kwargs.get('clientWeight')
        self.__hedgeAnnualizedVolatility = kwargs.get('hedgeAnnualizedVolatility')
        self.__benchmarkCurrency = kwargs.get('benchmarkCurrency')
        self.__name = kwargs.get('name')
        self.__aum = kwargs.get('aum')
        self.__folderName = kwargs.get('folderName')
        self.__lendingPartnerFee = kwargs.get('lendingPartnerFee')
        self.__region = kwargs.get('region')
        self.__liveDate = kwargs.get('liveDate')
        self.__askHigh = kwargs.get('askHigh')
        self.__corporateActionType = kwargs.get('corporateActionType')
        self.__primeId = kwargs.get('primeId')
        self.__tenor2 = kwargs.get('tenor2')
        self.__description = kwargs.get('description')
        self.__valueRevised = kwargs.get('valueRevised')
        self.__ownerName = kwargs.get('ownerName')
        self.__adjustedTradePrice = kwargs.get('adjustedTradePrice')
        self.__lastUpdatedById = kwargs.get('lastUpdatedById')
        self.__zScore = kwargs.get('zScore')
        self.__targetShareholderMeetingDate = kwargs.get('targetShareholderMeetingDate')
        self.__collateralMarketValue = kwargs.get('collateralMarketValue')
        self.__isADR = kwargs.get('isADR')
        self.__eventStartTime = kwargs.get('eventStartTime')
        self.__factor = kwargs.get('factor')
        self.__daysOnLoan = kwargs.get('daysOnLoan')
        self.__longConvictionSmall = kwargs.get('longConvictionSmall')
        self.__serviceId = kwargs.get('serviceId')
        self.__turnover = kwargs.get('turnover')
        self.__gsfeer = kwargs.get('gsfeer')
        self.__coverage = kwargs.get('coverage')
        self.__backtestId = kwargs.get('backtestId')
        self.__gPercentile = kwargs.get('gPercentile')
        self.__gScore = kwargs.get('gScore')
        self.__marketValue = kwargs.get('marketValue')
        self.__multipleScore = kwargs.get('multipleScore')
        self.__lendingFundNav = kwargs.get('lendingFundNav')
        self.__sourceOriginalCategory = kwargs.get('sourceOriginalCategory')
        self.__betaAdjustedExposure = kwargs.get('betaAdjustedExposure')
        self.__composite5DayAdv = kwargs.get('composite5DayAdv')
        self.__dividendPoints = kwargs.get('dividendPoints')
        self.__newIdeasWtd = kwargs.get('newIdeasWtd')
        self.__paid = kwargs.get('paid')
        self.__short = kwargs.get('short')
        self.__location = kwargs.get('location')
        self.__comment = kwargs.get('comment')
        self.__bosInTicksDescription = kwargs.get('bosInTicksDescription')
        self.__sourceSymbol = kwargs.get('sourceSymbol')
        self.__scenarioId = kwargs.get('scenarioId')
        self.__askUnadjusted = kwargs.get('askUnadjusted')
        self.__queueClockTime = kwargs.get('queueClockTime')
        self.__askChange = kwargs.get('askChange')
        self.__impliedCorrelation = kwargs.get('impliedCorrelation')
        self.__tcmCostParticipationRate50Pct = kwargs.get('tcmCostParticipationRate50Pct')
        self.__normalizedPerformance = kwargs.get('normalizedPerformance')
        self.__cmId = kwargs.get('cmId')
        self.__type = kwargs.get('type')
        self.__mdapi = kwargs.get('mdapi')
        self.__dividendYield = kwargs.get('dividendYield')
        self.__cumulativePnl = kwargs.get('cumulativePnl')
        self.__sourceOrigin = kwargs.get('sourceOrigin')
        self.__shortTenor = kwargs.get('shortTenor')
        self.__loss = kwargs.get('loss')
        self.__unadjustedVolume = kwargs.get('unadjustedVolume')
        self.__measures = kwargs.get('measures')
        self.__tradingCostPnl = kwargs.get('tradingCostPnl')
        self.__internalUser = kwargs.get('internalUser')
        self.__price = kwargs.get('price')
        self.__paymentQuantity = kwargs.get('paymentQuantity')
        self.__underlyer = kwargs.get('underlyer')
        self.__positionIdx = kwargs.get('positionIdx')
        self.__secName = kwargs.get('secName')
        self.__percentADV = kwargs.get('percentADV')
        self.__redemptionOption = kwargs.get('redemptionOption')
        self.__unadjustedLow = kwargs.get('unadjustedLow')
        self.__contract = kwargs.get('contract')
        self.__sedol = kwargs.get('sedol')
        self.__roundingCostPnl = kwargs.get('roundingCostPnl')
        self.__sustainGlobal = kwargs.get('sustainGlobal')
        self.__sourceTicker = kwargs.get('sourceTicker')
        self.__portfolioId = kwargs.get('portfolioId')
        self.__gsid = kwargs.get('gsid')
        self.__esPercentile = kwargs.get('esPercentile')
        self.__lendingFund = kwargs.get('lendingFund')
        self.__tcmCostParticipationRate15Pct = kwargs.get('tcmCostParticipationRate15Pct')
        self.__sensitivity = kwargs.get('sensitivity')
        self.__fiscalYear = kwargs.get('fiscalYear')
        self.__rcic = kwargs.get('rcic')
        self.__simonAssetTags = kwargs.get('simonAssetTags')
        self.__internal = kwargs.get('internal')
        self.__forwardPoint = kwargs.get('forwardPoint')
        self.__assetClassificationsGicsIndustry = kwargs.get('assetClassificationsGicsIndustry')
        self.__adjustedBidPrice = kwargs.get('adjustedBidPrice')
        self.__hitRateQtd = kwargs.get('hitRateQtd')
        self.__varSwap = kwargs.get('varSwap')
        self.__lowUnadjusted = kwargs.get('lowUnadjusted')
        self.__sectorsRaw = kwargs.get('sectorsRaw')
        self.__recallQuantity = kwargs.get('recallQuantity')
        self.__low = kwargs.get('low')
        self.__crossGroup = kwargs.get('crossGroup')
        self.__integratedScore = kwargs.get('integratedScore')
        self.__fiveDayPriceChangeBps = kwargs.get('fiveDayPriceChangeBps')
        self.__tradeSize = kwargs.get('tradeSize')
        self.__holdings = kwargs.get('holdings')
        self.__symbolDimensions = kwargs.get('symbolDimensions')
        self.__priceMethod = kwargs.get('priceMethod')
        self.__quotingStyle = kwargs.get('quotingStyle')
        self.__scenarioGroupId = kwargs.get('scenarioGroupId')
        self.__errorMessage = kwargs.get('errorMessage')
        self.__averageImpliedVariance = kwargs.get('averageImpliedVariance')
        self.__avgTradeRateDescription = kwargs.get('avgTradeRateDescription')
        self.__midPrice = kwargs.get('midPrice')
        self.__fraction = kwargs.get('fraction')
        self.__stsCreditMarket = kwargs.get('stsCreditMarket')
        self.__assetCountShort = kwargs.get('assetCountShort')
        self.__stsEmDm = kwargs.get('stsEmDm')
        self.__requiredCollateralValue = kwargs.get('requiredCollateralValue')
        self.__tcmCostHorizon2Day = kwargs.get('tcmCostHorizon2Day')
        self.__pendingLoanCount = kwargs.get('pendingLoanCount')
        self.__queueInLots = kwargs.get('queueInLots')
        self.__priceRangeInTicksDescription = kwargs.get('priceRangeInTicksDescription')
        self.__tenderOfferExpirationDate = kwargs.get('tenderOfferExpirationDate')
        self.__highUnadjusted = kwargs.get('highUnadjusted')
        self.__sourceCategory = kwargs.get('sourceCategory')
        self.__volumeUnadjusted = kwargs.get('volumeUnadjusted')
        self.__avgTradeRateLabel = kwargs.get('avgTradeRateLabel')
        self.__tcmCostParticipationRate5Pct = kwargs.get('tcmCostParticipationRate5Pct')
        self.__isActive = kwargs.get('isActive')
        self.__growthScore = kwargs.get('growthScore')
        self.__bufferThreshold = kwargs.get('bufferThreshold')
        self.__encodedStats = kwargs.get('encodedStats')
        self.__adjustedShortInterest = kwargs.get('adjustedShortInterest')
        self.__askSize = kwargs.get('askSize')
        self.__mdapiType = kwargs.get('mdapiType')
        self.__group = kwargs.get('group')
        self.__estimatedSpread = kwargs.get('estimatedSpread')
        self.__resource = kwargs.get('resource')
        self.__averageRealizedVolatility = kwargs.get('averageRealizedVolatility')
        self.__tcmCost = kwargs.get('tcmCost')
        self.__sustainJapan = kwargs.get('sustainJapan')
        self.__navSpread = kwargs.get('navSpread')
        self.__bidPrice = kwargs.get('bidPrice')
        self.__dollarTotalReturn = kwargs.get('dollarTotalReturn')
        self.__hedgeTrackingError = kwargs.get('hedgeTrackingError')
        self.__marketCapCategory = kwargs.get('marketCapCategory')
        self.__historicalVolume = kwargs.get('historicalVolume')
        self.__esNumericPercentile = kwargs.get('esNumericPercentile')
        self.__strikePrice = kwargs.get('strikePrice')
        self.__askGspread = kwargs.get('askGspread')
        self.__calSpreadMisPricing = kwargs.get('calSpreadMisPricing')
        self.__equityGamma = kwargs.get('equityGamma')
        self.__grossIncome = kwargs.get('grossIncome')
        self.__emId = kwargs.get('emId')
        self.__adjustedOpenPrice = kwargs.get('adjustedOpenPrice')
        self.__assetCountInModel = kwargs.get('assetCountInModel')
        self.__stsCreditRegion = kwargs.get('stsCreditRegion')
        self.__point = kwargs.get('point')
        self.__totalReturns = kwargs.get('totalReturns')
        self.__lender = kwargs.get('lender')
        self.__minTemperature = kwargs.get('minTemperature')
        self.__value = kwargs.get('value')
        self.__relativeStrike = kwargs.get('relativeStrike')
        self.__amount = kwargs.get('amount')
        self.__quantity = kwargs.get('quantity')
        self.__lendingFundAcct = kwargs.get('lendingFundAcct')
        self.__reportId = kwargs.get('reportId')
        self.__indexWeight = kwargs.get('indexWeight')
        self.__rebate = kwargs.get('rebate')
        self.__flagship = kwargs.get('flagship')
        self.__trader = kwargs.get('trader')
        self.__factorCategory = kwargs.get('factorCategory')
        self.__impliedVolatility = kwargs.get('impliedVolatility')
        self.__spread = kwargs.get('spread')
        self.__stsRatesMaturity = kwargs.get('stsRatesMaturity')
        self.__equityDelta = kwargs.get('equityDelta')
        self.__grossWeight = kwargs.get('grossWeight')
        self.__listed = kwargs.get('listed')
        self.__variance = kwargs.get('variance')
        self.__tcmCostHorizon6Hour = kwargs.get('tcmCostHorizon6Hour')
        self.__g10Currency = kwargs.get('g10Currency')
        self.__shockStyle = kwargs.get('shockStyle')
        self.__relativePeriod = kwargs.get('relativePeriod')
        self.__isin = kwargs.get('isin')
        self.__methodology = kwargs.get('methodology')

    @property
    def queueClockTimeLabel(self) -> tuple:
        return self.__queueClockTimeLabel

    @queueClockTimeLabel.setter
    def queueClockTimeLabel(self, value: tuple):
        self.__queueClockTimeLabel = value
        self._property_changed('queueClockTimeLabel')        

    @property
    def marketPnl(self) -> dict:
        return self.__marketPnl

    @marketPnl.setter
    def marketPnl(self, value: dict):
        self.__marketPnl = value
        self._property_changed('marketPnl')        

    @property
    def year(self) -> dict:
        return self.__year

    @year.setter
    def year(self, value: dict):
        self.__year = value
        self._property_changed('year')        

    @property
    def sustainAsiaExJapan(self) -> dict:
        return self.__sustainAsiaExJapan

    @sustainAsiaExJapan.setter
    def sustainAsiaExJapan(self, value: dict):
        self.__sustainAsiaExJapan = value
        self._property_changed('sustainAsiaExJapan')        

    @property
    def investmentRate(self) -> dict:
        return self.__investmentRate

    @investmentRate.setter
    def investmentRate(self, value: dict):
        self.__investmentRate = value
        self._property_changed('investmentRate')        

    @property
    def assetClassificationsGicsSubIndustry(self) -> dict:
        return self.__assetClassificationsGicsSubIndustry

    @assetClassificationsGicsSubIndustry.setter
    def assetClassificationsGicsSubIndustry(self, value: dict):
        self.__assetClassificationsGicsSubIndustry = value
        self._property_changed('assetClassificationsGicsSubIndustry')        

    @property
    def mdapiClass(self) -> dict:
        return self.__mdapiClass

    @mdapiClass.setter
    def mdapiClass(self, value: dict):
        self.__mdapiClass = value
        self._property_changed('mdapiClass')        

    @property
    def bidUnadjusted(self) -> dict:
        return self.__bidUnadjusted

    @bidUnadjusted.setter
    def bidUnadjusted(self, value: dict):
        self.__bidUnadjusted = value
        self._property_changed('bidUnadjusted')        

    @property
    def economicTermsHash(self) -> dict:
        return self.__economicTermsHash

    @economicTermsHash.setter
    def economicTermsHash(self, value: dict):
        self.__economicTermsHash = value
        self._property_changed('economicTermsHash')        

    @property
    def neighbourAssetId(self) -> dict:
        return self.__neighbourAssetId

    @neighbourAssetId.setter
    def neighbourAssetId(self, value: dict):
        self.__neighbourAssetId = value
        self._property_changed('neighbourAssetId')        

    @property
    def simonIntlAssetTags(self) -> dict:
        return self.__simonIntlAssetTags

    @simonIntlAssetTags.setter
    def simonIntlAssetTags(self, value: dict):
        self.__simonIntlAssetTags = value
        self._property_changed('simonIntlAssetTags')        

    @property
    def path(self) -> dict:
        return self.__path

    @path.setter
    def path(self, value: dict):
        self.__path = value
        self._property_changed('path')        

    @property
    def availableInventory(self) -> dict:
        return self.__availableInventory

    @availableInventory.setter
    def availableInventory(self, value: dict):
        self.__availableInventory = value
        self._property_changed('availableInventory')        

    @property
    def clientContact(self) -> dict:
        return self.__clientContact

    @clientContact.setter
    def clientContact(self, value: dict):
        self.__clientContact = value
        self._property_changed('clientContact')        

    @property
    def est1DayCompletePct(self) -> dict:
        return self.__est1DayCompletePct

    @est1DayCompletePct.setter
    def est1DayCompletePct(self, value: dict):
        self.__est1DayCompletePct = value
        self._property_changed('est1DayCompletePct')        

    @property
    def rank(self) -> dict:
        return self.__rank

    @rank.setter
    def rank(self, value: dict):
        self.__rank = value
        self._property_changed('rank')        

    @property
    def dataSetCategory(self) -> dict:
        return self.__dataSetCategory

    @dataSetCategory.setter
    def dataSetCategory(self, value: dict):
        self.__dataSetCategory = value
        self._property_changed('dataSetCategory')        

    @property
    def createdById(self) -> dict:
        return self.__createdById

    @createdById.setter
    def createdById(self, value: dict):
        self.__createdById = value
        self._property_changed('createdById')        

    @property
    def vehicleType(self) -> dict:
        return self.__vehicleType

    @vehicleType.setter
    def vehicleType(self, value: dict):
        self.__vehicleType = value
        self._property_changed('vehicleType')        

    @property
    def dailyRisk(self) -> dict:
        return self.__dailyRisk

    @dailyRisk.setter
    def dailyRisk(self, value: dict):
        self.__dailyRisk = value
        self._property_changed('dailyRisk')        

    @property
    def bosInBpsLabel(self) -> tuple:
        return self.__bosInBpsLabel

    @bosInBpsLabel.setter
    def bosInBpsLabel(self, value: tuple):
        self.__bosInBpsLabel = value
        self._property_changed('bosInBpsLabel')        

    @property
    def energy(self) -> dict:
        return self.__energy

    @energy.setter
    def energy(self, value: dict):
        self.__energy = value
        self._property_changed('energy')        

    @property
    def marketDataType(self) -> dict:
        return self.__marketDataType

    @marketDataType.setter
    def marketDataType(self, value: dict):
        self.__marketDataType = value
        self._property_changed('marketDataType')        

    @property
    def sentimentScore(self) -> dict:
        return self.__sentimentScore

    @sentimentScore.setter
    def sentimentScore(self, value: dict):
        self.__sentimentScore = value
        self._property_changed('sentimentScore')        

    @property
    def bosInBps(self) -> dict:
        return self.__bosInBps

    @bosInBps.setter
    def bosInBps(self, value: dict):
        self.__bosInBps = value
        self._property_changed('bosInBps')        

    @property
    def pointClass(self) -> dict:
        return self.__pointClass

    @pointClass.setter
    def pointClass(self, value: dict):
        self.__pointClass = value
        self._property_changed('pointClass')        

    @property
    def fxSpot(self) -> dict:
        return self.__fxSpot

    @fxSpot.setter
    def fxSpot(self, value: dict):
        self.__fxSpot = value
        self._property_changed('fxSpot')        

    @property
    def bidLow(self) -> dict:
        return self.__bidLow

    @bidLow.setter
    def bidLow(self, value: dict):
        self.__bidLow = value
        self._property_changed('bidLow')        

    @property
    def valuePrevious(self) -> dict:
        return self.__valuePrevious

    @valuePrevious.setter
    def valuePrevious(self, value: dict):
        self.__valuePrevious = value
        self._property_changed('valuePrevious')        

    @property
    def fairVarianceVolatility(self) -> dict:
        return self.__fairVarianceVolatility

    @fairVarianceVolatility.setter
    def fairVarianceVolatility(self, value: dict):
        self.__fairVarianceVolatility = value
        self._property_changed('fairVarianceVolatility')        

    @property
    def avgTradeRate(self) -> dict:
        return self.__avgTradeRate

    @avgTradeRate.setter
    def avgTradeRate(self, value: dict):
        self.__avgTradeRate = value
        self._property_changed('avgTradeRate')        

    @property
    def shortLevel(self) -> dict:
        return self.__shortLevel

    @shortLevel.setter
    def shortLevel(self, value: dict):
        self.__shortLevel = value
        self._property_changed('shortLevel')        

    @property
    def hedgeVolatility(self) -> dict:
        return self.__hedgeVolatility

    @hedgeVolatility.setter
    def hedgeVolatility(self, value: dict):
        self.__hedgeVolatility = value
        self._property_changed('hedgeVolatility')        

    @property
    def version(self) -> dict:
        return self.__version

    @version.setter
    def version(self, value: dict):
        self.__version = value
        self._property_changed('version')        

    @property
    def tags(self) -> dict:
        return self.__tags

    @tags.setter
    def tags(self, value: dict):
        self.__tags = value
        self._property_changed('tags')        

    @property
    def underlyingAssetId(self) -> dict:
        return self.__underlyingAssetId

    @underlyingAssetId.setter
    def underlyingAssetId(self, value: dict):
        self.__underlyingAssetId = value
        self._property_changed('underlyingAssetId')        

    @property
    def clientExposure(self) -> dict:
        return self.__clientExposure

    @clientExposure.setter
    def clientExposure(self, value: dict):
        self.__clientExposure = value
        self._property_changed('clientExposure')        

    @property
    def correlation(self) -> dict:
        return self.__correlation

    @correlation.setter
    def correlation(self, value: dict):
        self.__correlation = value
        self._property_changed('correlation')        

    @property
    def exposure(self) -> dict:
        return self.__exposure

    @exposure.setter
    def exposure(self, value: dict):
        self.__exposure = value
        self._property_changed('exposure')        

    @property
    def gsSustainSubSector(self) -> dict:
        return self.__gsSustainSubSector

    @gsSustainSubSector.setter
    def gsSustainSubSector(self, value: dict):
        self.__gsSustainSubSector = value
        self._property_changed('gsSustainSubSector')        

    @property
    def domain(self) -> dict:
        return self.__domain

    @domain.setter
    def domain(self, value: dict):
        self.__domain = value
        self._property_changed('domain')        

    @property
    def marketDataAsset(self) -> dict:
        return self.__marketDataAsset

    @marketDataAsset.setter
    def marketDataAsset(self, value: dict):
        self.__marketDataAsset = value
        self._property_changed('marketDataAsset')        

    @property
    def forwardTenor(self) -> dict:
        return self.__forwardTenor

    @forwardTenor.setter
    def forwardTenor(self, value: dict):
        self.__forwardTenor = value
        self._property_changed('forwardTenor')        

    @property
    def unadjustedHigh(self) -> dict:
        return self.__unadjustedHigh

    @unadjustedHigh.setter
    def unadjustedHigh(self, value: dict):
        self.__unadjustedHigh = value
        self._property_changed('unadjustedHigh')        

    @property
    def sourceImportance(self) -> dict:
        return self.__sourceImportance

    @sourceImportance.setter
    def sourceImportance(self, value: dict):
        self.__sourceImportance = value
        self._property_changed('sourceImportance')        

    @property
    def eid(self) -> dict:
        return self.__eid

    @eid.setter
    def eid(self, value: dict):
        self.__eid = value
        self._property_changed('eid')        

    @property
    def jsn(self) -> dict:
        return self.__jsn

    @jsn.setter
    def jsn(self, value: dict):
        self.__jsn = value
        self._property_changed('jsn')        

    @property
    def relativeReturnQtd(self) -> dict:
        return self.__relativeReturnQtd

    @relativeReturnQtd.setter
    def relativeReturnQtd(self, value: dict):
        self.__relativeReturnQtd = value
        self._property_changed('relativeReturnQtd')        

    @property
    def displayName(self) -> dict:
        return self.__displayName

    @displayName.setter
    def displayName(self, value: dict):
        self.__displayName = value
        self._property_changed('displayName')        

    @property
    def minutesToTrade100Pct(self) -> dict:
        return self.__minutesToTrade100Pct

    @minutesToTrade100Pct.setter
    def minutesToTrade100Pct(self, value: dict):
        self.__minutesToTrade100Pct = value
        self._property_changed('minutesToTrade100Pct')        

    @property
    def marketModelId(self) -> dict:
        return self.__marketModelId

    @marketModelId.setter
    def marketModelId(self, value: dict):
        self.__marketModelId = value
        self._property_changed('marketModelId')        

    @property
    def quoteType(self) -> dict:
        return self.__quoteType

    @quoteType.setter
    def quoteType(self, value: dict):
        self.__quoteType = value
        self._property_changed('quoteType')        

    @property
    def realizedCorrelation(self) -> dict:
        return self.__realizedCorrelation

    @realizedCorrelation.setter
    def realizedCorrelation(self, value: dict):
        self.__realizedCorrelation = value
        self._property_changed('realizedCorrelation')        

    @property
    def tenor(self) -> dict:
        return self.__tenor

    @tenor.setter
    def tenor(self, value: dict):
        self.__tenor = value
        self._property_changed('tenor')        

    @property
    def esPolicyPercentile(self) -> dict:
        return self.__esPolicyPercentile

    @esPolicyPercentile.setter
    def esPolicyPercentile(self, value: dict):
        self.__esPolicyPercentile = value
        self._property_changed('esPolicyPercentile')        

    @property
    def atmFwdRate(self) -> dict:
        return self.__atmFwdRate

    @atmFwdRate.setter
    def atmFwdRate(self, value: dict):
        self.__atmFwdRate = value
        self._property_changed('atmFwdRate')        

    @property
    def tcmCostParticipationRate75Pct(self) -> dict:
        return self.__tcmCostParticipationRate75Pct

    @tcmCostParticipationRate75Pct.setter
    def tcmCostParticipationRate75Pct(self, value: dict):
        self.__tcmCostParticipationRate75Pct = value
        self._property_changed('tcmCostParticipationRate75Pct')        

    @property
    def close(self) -> dict:
        return self.__close

    @close.setter
    def close(self, value: dict):
        self.__close = value
        self._property_changed('close')        

    @property
    def tcmCostParticipationRate100Pct(self) -> dict:
        return self.__tcmCostParticipationRate100Pct

    @tcmCostParticipationRate100Pct.setter
    def tcmCostParticipationRate100Pct(self, value: dict):
        self.__tcmCostParticipationRate100Pct = value
        self._property_changed('tcmCostParticipationRate100Pct')        

    @property
    def disclaimer(self) -> dict:
        return self.__disclaimer

    @disclaimer.setter
    def disclaimer(self, value: dict):
        self.__disclaimer = value
        self._property_changed('disclaimer')        

    @property
    def measureIdx(self) -> dict:
        return self.__measureIdx

    @measureIdx.setter
    def measureIdx(self, value: dict):
        self.__measureIdx = value
        self._property_changed('measureIdx')        

    @property
    def a(self) -> dict:
        return self.__a

    @a.setter
    def a(self, value: dict):
        self.__a = value
        self._property_changed('a')        

    @property
    def b(self) -> dict:
        return self.__b

    @b.setter
    def b(self, value: dict):
        self.__b = value
        self._property_changed('b')        

    @property
    def loanFee(self) -> dict:
        return self.__loanFee

    @loanFee.setter
    def loanFee(self, value: dict):
        self.__loanFee = value
        self._property_changed('loanFee')        

    @property
    def c(self) -> dict:
        return self.__c

    @c.setter
    def c(self, value: dict):
        self.__c = value
        self._property_changed('c')        

    @property
    def equityVega(self) -> dict:
        return self.__equityVega

    @equityVega.setter
    def equityVega(self, value: dict):
        self.__equityVega = value
        self._property_changed('equityVega')        

    @property
    def lenderPayment(self) -> dict:
        return self.__lenderPayment

    @lenderPayment.setter
    def lenderPayment(self, value: dict):
        self.__lenderPayment = value
        self._property_changed('lenderPayment')        

    @property
    def deploymentVersion(self) -> dict:
        return self.__deploymentVersion

    @deploymentVersion.setter
    def deploymentVersion(self, value: dict):
        self.__deploymentVersion = value
        self._property_changed('deploymentVersion')        

    @property
    def fiveDayMove(self) -> dict:
        return self.__fiveDayMove

    @fiveDayMove.setter
    def fiveDayMove(self, value: dict):
        self.__fiveDayMove = value
        self._property_changed('fiveDayMove')        

    @property
    def borrower(self) -> dict:
        return self.__borrower

    @borrower.setter
    def borrower(self, value: dict):
        self.__borrower = value
        self._property_changed('borrower')        

    @property
    def valueFormat(self) -> dict:
        return self.__valueFormat

    @valueFormat.setter
    def valueFormat(self, value: dict):
        self.__valueFormat = value
        self._property_changed('valueFormat')        

    @property
    def performanceContribution(self) -> dict:
        return self.__performanceContribution

    @performanceContribution.setter
    def performanceContribution(self, value: dict):
        self.__performanceContribution = value
        self._property_changed('performanceContribution')        

    @property
    def targetNotional(self) -> dict:
        return self.__targetNotional

    @targetNotional.setter
    def targetNotional(self, value: dict):
        self.__targetNotional = value
        self._property_changed('targetNotional')        

    @property
    def fillLegId(self) -> dict:
        return self.__fillLegId

    @fillLegId.setter
    def fillLegId(self, value: dict):
        self.__fillLegId = value
        self._property_changed('fillLegId')        

    @property
    def delisted(self) -> dict:
        return self.__delisted

    @delisted.setter
    def delisted(self, value: dict):
        self.__delisted = value
        self._property_changed('delisted')        

    @property
    def rationale(self) -> dict:
        return self.__rationale

    @rationale.setter
    def rationale(self, value: dict):
        self.__rationale = value
        self._property_changed('rationale')        

    @property
    def regionalFocus(self) -> dict:
        return self.__regionalFocus

    @regionalFocus.setter
    def regionalFocus(self, value: dict):
        self.__regionalFocus = value
        self._property_changed('regionalFocus')        

    @property
    def volumePrimary(self) -> dict:
        return self.__volumePrimary

    @volumePrimary.setter
    def volumePrimary(self, value: dict):
        self.__volumePrimary = value
        self._property_changed('volumePrimary')        

    @property
    def series(self) -> dict:
        return self.__series

    @series.setter
    def series(self, value: dict):
        self.__series = value
        self._property_changed('series')        

    @property
    def simonId(self) -> dict:
        return self.__simonId

    @simonId.setter
    def simonId(self, value: dict):
        self.__simonId = value
        self._property_changed('simonId')        

    @property
    def newIdeasQtd(self) -> dict:
        return self.__newIdeasQtd

    @newIdeasQtd.setter
    def newIdeasQtd(self, value: dict):
        self.__newIdeasQtd = value
        self._property_changed('newIdeasQtd')        

    @property
    def congestion(self) -> dict:
        return self.__congestion

    @congestion.setter
    def congestion(self, value: dict):
        self.__congestion = value
        self._property_changed('congestion')        

    @property
    def adjustedAskPrice(self) -> dict:
        return self.__adjustedAskPrice

    @adjustedAskPrice.setter
    def adjustedAskPrice(self, value: dict):
        self.__adjustedAskPrice = value
        self._property_changed('adjustedAskPrice')        

    @property
    def quarter(self) -> dict:
        return self.__quarter

    @quarter.setter
    def quarter(self, value: dict):
        self.__quarter = value
        self._property_changed('quarter')        

    @property
    def factorUniverse(self) -> dict:
        return self.__factorUniverse

    @factorUniverse.setter
    def factorUniverse(self, value: dict):
        self.__factorUniverse = value
        self._property_changed('factorUniverse')        

    @property
    def eventCategory(self) -> dict:
        return self.__eventCategory

    @eventCategory.setter
    def eventCategory(self, value: dict):
        self.__eventCategory = value
        self._property_changed('eventCategory')        

    @property
    def impliedNormalVolatility(self) -> dict:
        return self.__impliedNormalVolatility

    @impliedNormalVolatility.setter
    def impliedNormalVolatility(self, value: dict):
        self.__impliedNormalVolatility = value
        self._property_changed('impliedNormalVolatility')        

    @property
    def unadjustedOpen(self) -> dict:
        return self.__unadjustedOpen

    @unadjustedOpen.setter
    def unadjustedOpen(self, value: dict):
        self.__unadjustedOpen = value
        self._property_changed('unadjustedOpen')        

    @property
    def arrivalRt(self) -> dict:
        return self.__arrivalRt

    @arrivalRt.setter
    def arrivalRt(self, value: dict):
        self.__arrivalRt = value
        self._property_changed('arrivalRt')        

    @property
    def criticality(self) -> dict:
        return self.__criticality

    @criticality.setter
    def criticality(self, value: dict):
        self.__criticality = value
        self._property_changed('criticality')        

    @property
    def transactionCost(self) -> dict:
        return self.__transactionCost

    @transactionCost.setter
    def transactionCost(self, value: dict):
        self.__transactionCost = value
        self._property_changed('transactionCost')        

    @property
    def servicingCostShortPnl(self) -> dict:
        return self.__servicingCostShortPnl

    @servicingCostShortPnl.setter
    def servicingCostShortPnl(self, value: dict):
        self.__servicingCostShortPnl = value
        self._property_changed('servicingCostShortPnl')        

    @property
    def bidAskSpread(self) -> dict:
        return self.__bidAskSpread

    @bidAskSpread.setter
    def bidAskSpread(self, value: dict):
        self.__bidAskSpread = value
        self._property_changed('bidAskSpread')        

    @property
    def optionType(self) -> dict:
        return self.__optionType

    @optionType.setter
    def optionType(self, value: dict):
        self.__optionType = value
        self._property_changed('optionType')        

    @property
    def tcmCostHorizon3Hour(self) -> dict:
        return self.__tcmCostHorizon3Hour

    @tcmCostHorizon3Hour.setter
    def tcmCostHorizon3Hour(self, value: dict):
        self.__tcmCostHorizon3Hour = value
        self._property_changed('tcmCostHorizon3Hour')        

    @property
    def clusterDescription(self) -> dict:
        return self.__clusterDescription

    @clusterDescription.setter
    def clusterDescription(self, value: dict):
        self.__clusterDescription = value
        self._property_changed('clusterDescription')        

    @property
    def creditLimit(self) -> dict:
        return self.__creditLimit

    @creditLimit.setter
    def creditLimit(self, value: dict):
        self.__creditLimit = value
        self._property_changed('creditLimit')        

    @property
    def positionAmount(self) -> dict:
        return self.__positionAmount

    @positionAmount.setter
    def positionAmount(self, value: dict):
        self.__positionAmount = value
        self._property_changed('positionAmount')        

    @property
    def numberOfPositions(self) -> dict:
        return self.__numberOfPositions

    @numberOfPositions.setter
    def numberOfPositions(self, value: dict):
        self.__numberOfPositions = value
        self._property_changed('numberOfPositions')        

    @property
    def windSpeed(self) -> dict:
        return self.__windSpeed

    @windSpeed.setter
    def windSpeed(self, value: dict):
        self.__windSpeed = value
        self._property_changed('windSpeed')        

    @property
    def openUnadjusted(self) -> dict:
        return self.__openUnadjusted

    @openUnadjusted.setter
    def openUnadjusted(self, value: dict):
        self.__openUnadjusted = value
        self._property_changed('openUnadjusted')        

    @property
    def maRank(self) -> dict:
        return self.__maRank

    @maRank.setter
    def maRank(self, value: dict):
        self.__maRank = value
        self._property_changed('maRank')        

    @property
    def askPrice(self) -> dict:
        return self.__askPrice

    @askPrice.setter
    def askPrice(self, value: dict):
        self.__askPrice = value
        self._property_changed('askPrice')        

    @property
    def eventId(self) -> dict:
        return self.__eventId

    @eventId.setter
    def eventId(self, value: dict):
        self.__eventId = value
        self._property_changed('eventId')        

    @property
    def borrowerId(self) -> dict:
        return self.__borrowerId

    @borrowerId.setter
    def borrowerId(self, value: dict):
        self.__borrowerId = value
        self._property_changed('borrowerId')        

    @property
    def dataProduct(self) -> dict:
        return self.__dataProduct

    @dataProduct.setter
    def dataProduct(self, value: dict):
        self.__dataProduct = value
        self._property_changed('dataProduct')        

    @property
    def sectors(self) -> dict:
        return self.__sectors

    @sectors.setter
    def sectors(self, value: dict):
        self.__sectors = value
        self._property_changed('sectors')        

    @property
    def mqSymbol(self) -> dict:
        return self.__mqSymbol

    @mqSymbol.setter
    def mqSymbol(self, value: dict):
        self.__mqSymbol = value
        self._property_changed('mqSymbol')        

    @property
    def annualizedTrackingError(self) -> dict:
        return self.__annualizedTrackingError

    @annualizedTrackingError.setter
    def annualizedTrackingError(self, value: dict):
        self.__annualizedTrackingError = value
        self._property_changed('annualizedTrackingError')        

    @property
    def volSwap(self) -> dict:
        return self.__volSwap

    @volSwap.setter
    def volSwap(self, value: dict):
        self.__volSwap = value
        self._property_changed('volSwap')        

    @property
    def annualizedRisk(self) -> dict:
        return self.__annualizedRisk

    @annualizedRisk.setter
    def annualizedRisk(self, value: dict):
        self.__annualizedRisk = value
        self._property_changed('annualizedRisk')        

    @property
    def bmPrimeId(self) -> dict:
        return self.__bmPrimeId

    @bmPrimeId.setter
    def bmPrimeId(self, value: dict):
        self.__bmPrimeId = value
        self._property_changed('bmPrimeId')        

    @property
    def corporateAction(self) -> dict:
        return self.__corporateAction

    @corporateAction.setter
    def corporateAction(self, value: dict):
        self.__corporateAction = value
        self._property_changed('corporateAction')        

    @property
    def conviction(self) -> dict:
        return self.__conviction

    @conviction.setter
    def conviction(self, value: dict):
        self.__conviction = value
        self._property_changed('conviction')        

    @property
    def grossExposure(self) -> dict:
        return self.__grossExposure

    @grossExposure.setter
    def grossExposure(self, value: dict):
        self.__grossExposure = value
        self._property_changed('grossExposure')        

    @property
    def benchmarkMaturity(self) -> dict:
        return self.__benchmarkMaturity

    @benchmarkMaturity.setter
    def benchmarkMaturity(self, value: dict):
        self.__benchmarkMaturity = value
        self._property_changed('benchmarkMaturity')        

    @property
    def gRegionalScore(self) -> dict:
        return self.__gRegionalScore

    @gRegionalScore.setter
    def gRegionalScore(self, value: dict):
        self.__gRegionalScore = value
        self._property_changed('gRegionalScore')        

    @property
    def volumeComposite(self) -> dict:
        return self.__volumeComposite

    @volumeComposite.setter
    def volumeComposite(self, value: dict):
        self.__volumeComposite = value
        self._property_changed('volumeComposite')        

    @property
    def volume(self) -> dict:
        return self.__volume

    @volume.setter
    def volume(self, value: dict):
        self.__volume = value
        self._property_changed('volume')        

    @property
    def factorId(self) -> dict:
        return self.__factorId

    @factorId.setter
    def factorId(self, value: dict):
        self.__factorId = value
        self._property_changed('factorId')        

    @property
    def hardToBorrow(self) -> dict:
        return self.__hardToBorrow

    @hardToBorrow.setter
    def hardToBorrow(self, value: dict):
        self.__hardToBorrow = value
        self._property_changed('hardToBorrow')        

    @property
    def adv(self) -> dict:
        return self.__adv

    @adv.setter
    def adv(self, value: dict):
        self.__adv = value
        self._property_changed('adv')        

    @property
    def stsFxCurrency(self) -> dict:
        return self.__stsFxCurrency

    @stsFxCurrency.setter
    def stsFxCurrency(self, value: dict):
        self.__stsFxCurrency = value
        self._property_changed('stsFxCurrency')        

    @property
    def wpk(self) -> dict:
        return self.__wpk

    @wpk.setter
    def wpk(self, value: dict):
        self.__wpk = value
        self._property_changed('wpk')        

    @property
    def shortConvictionMedium(self) -> dict:
        return self.__shortConvictionMedium

    @shortConvictionMedium.setter
    def shortConvictionMedium(self, value: dict):
        self.__shortConvictionMedium = value
        self._property_changed('shortConvictionMedium')        

    @property
    def bidChange(self) -> dict:
        return self.__bidChange

    @bidChange.setter
    def bidChange(self, value: dict):
        self.__bidChange = value
        self._property_changed('bidChange')        

    @property
    def exchange(self) -> dict:
        return self.__exchange

    @exchange.setter
    def exchange(self, value: dict):
        self.__exchange = value
        self._property_changed('exchange')        

    @property
    def expiration(self) -> dict:
        return self.__expiration

    @expiration.setter
    def expiration(self, value: dict):
        self.__expiration = value
        self._property_changed('expiration')        

    @property
    def tradePrice(self) -> dict:
        return self.__tradePrice

    @tradePrice.setter
    def tradePrice(self, value: dict):
        self.__tradePrice = value
        self._property_changed('tradePrice')        

    @property
    def esPolicyScore(self) -> dict:
        return self.__esPolicyScore

    @esPolicyScore.setter
    def esPolicyScore(self, value: dict):
        self.__esPolicyScore = value
        self._property_changed('esPolicyScore')        

    @property
    def loanId(self) -> dict:
        return self.__loanId

    @loanId.setter
    def loanId(self, value: dict):
        self.__loanId = value
        self._property_changed('loanId')        

    @property
    def primeIdNumeric(self) -> dict:
        return self.__primeIdNumeric

    @primeIdNumeric.setter
    def primeIdNumeric(self, value: dict):
        self.__primeIdNumeric = value
        self._property_changed('primeIdNumeric')        

    @property
    def cid(self) -> dict:
        return self.__cid

    @cid.setter
    def cid(self, value: dict):
        self.__cid = value
        self._property_changed('cid')        

    @property
    def onboarded(self) -> dict:
        return self.__onboarded

    @onboarded.setter
    def onboarded(self, value: dict):
        self.__onboarded = value
        self._property_changed('onboarded')        

    @property
    def liquidityScore(self) -> dict:
        return self.__liquidityScore

    @liquidityScore.setter
    def liquidityScore(self, value: dict):
        self.__liquidityScore = value
        self._property_changed('liquidityScore')        

    @property
    def importance(self) -> dict:
        return self.__importance

    @importance.setter
    def importance(self, value: dict):
        self.__importance = value
        self._property_changed('importance')        

    @property
    def sourceDateSpan(self) -> dict:
        return self.__sourceDateSpan

    @sourceDateSpan.setter
    def sourceDateSpan(self, value: dict):
        self.__sourceDateSpan = value
        self._property_changed('sourceDateSpan')        

    @property
    def assetClassificationsGicsSector(self) -> dict:
        return self.__assetClassificationsGicsSector

    @assetClassificationsGicsSector.setter
    def assetClassificationsGicsSector(self, value: dict):
        self.__assetClassificationsGicsSector = value
        self._property_changed('assetClassificationsGicsSector')        

    @property
    def underlyingDataSetId(self) -> dict:
        return self.__underlyingDataSetId

    @underlyingDataSetId.setter
    def underlyingDataSetId(self, value: dict):
        self.__underlyingDataSetId = value
        self._property_changed('underlyingDataSetId')        

    @property
    def stsAssetName(self) -> dict:
        return self.__stsAssetName

    @stsAssetName.setter
    def stsAssetName(self, value: dict):
        self.__stsAssetName = value
        self._property_changed('stsAssetName')        

    @property
    def closeUnadjusted(self) -> dict:
        return self.__closeUnadjusted

    @closeUnadjusted.setter
    def closeUnadjusted(self, value: dict):
        self.__closeUnadjusted = value
        self._property_changed('closeUnadjusted')        

    @property
    def valueUnit(self) -> dict:
        return self.__valueUnit

    @valueUnit.setter
    def valueUnit(self, value: dict):
        self.__valueUnit = value
        self._property_changed('valueUnit')        

    @property
    def bidHigh(self) -> dict:
        return self.__bidHigh

    @bidHigh.setter
    def bidHigh(self, value: dict):
        self.__bidHigh = value
        self._property_changed('bidHigh')        

    @property
    def adjustedLowPrice(self) -> dict:
        return self.__adjustedLowPrice

    @adjustedLowPrice.setter
    def adjustedLowPrice(self, value: dict):
        self.__adjustedLowPrice = value
        self._property_changed('adjustedLowPrice')        

    @property
    def netExposureClassification(self) -> dict:
        return self.__netExposureClassification

    @netExposureClassification.setter
    def netExposureClassification(self, value: dict):
        self.__netExposureClassification = value
        self._property_changed('netExposureClassification')        

    @property
    def longConvictionLarge(self) -> dict:
        return self.__longConvictionLarge

    @longConvictionLarge.setter
    def longConvictionLarge(self, value: dict):
        self.__longConvictionLarge = value
        self._property_changed('longConvictionLarge')        

    @property
    def fairVariance(self) -> dict:
        return self.__fairVariance

    @fairVariance.setter
    def fairVariance(self, value: dict):
        self.__fairVariance = value
        self._property_changed('fairVariance')        

    @property
    def hitRateWtd(self) -> dict:
        return self.__hitRateWtd

    @hitRateWtd.setter
    def hitRateWtd(self, value: dict):
        self.__hitRateWtd = value
        self._property_changed('hitRateWtd')        

    @property
    def oad(self) -> dict:
        return self.__oad

    @oad.setter
    def oad(self, value: dict):
        self.__oad = value
        self._property_changed('oad')        

    @property
    def bosInBpsDescription(self) -> dict:
        return self.__bosInBpsDescription

    @bosInBpsDescription.setter
    def bosInBpsDescription(self, value: dict):
        self.__bosInBpsDescription = value
        self._property_changed('bosInBpsDescription')        

    @property
    def lowPrice(self) -> dict:
        return self.__lowPrice

    @lowPrice.setter
    def lowPrice(self, value: dict):
        self.__lowPrice = value
        self._property_changed('lowPrice')        

    @property
    def realizedVolatility(self) -> dict:
        return self.__realizedVolatility

    @realizedVolatility.setter
    def realizedVolatility(self, value: dict):
        self.__realizedVolatility = value
        self._property_changed('realizedVolatility')        

    @property
    def rate(self) -> dict:
        return self.__rate

    @rate.setter
    def rate(self, value: dict):
        self.__rate = value
        self._property_changed('rate')        

    @property
    def adv22DayPct(self) -> dict:
        return self.__adv22DayPct

    @adv22DayPct.setter
    def adv22DayPct(self, value: dict):
        self.__adv22DayPct = value
        self._property_changed('adv22DayPct')        

    @property
    def alpha(self) -> dict:
        return self.__alpha

    @alpha.setter
    def alpha(self, value: dict):
        self.__alpha = value
        self._property_changed('alpha')        

    @property
    def client(self) -> dict:
        return self.__client

    @client.setter
    def client(self, value: dict):
        self.__client = value
        self._property_changed('client')        

    @property
    def cloneParentId(self) -> dict:
        return self.__cloneParentId

    @cloneParentId.setter
    def cloneParentId(self, value: dict):
        self.__cloneParentId = value
        self._property_changed('cloneParentId')        

    @property
    def company(self) -> dict:
        return self.__company

    @company.setter
    def company(self, value: dict):
        self.__company = value
        self._property_changed('company')        

    @property
    def convictionList(self) -> dict:
        return self.__convictionList

    @convictionList.setter
    def convictionList(self, value: dict):
        self.__convictionList = value
        self._property_changed('convictionList')        

    @property
    def priceRangeInTicksLabel(self) -> tuple:
        return self.__priceRangeInTicksLabel

    @priceRangeInTicksLabel.setter
    def priceRangeInTicksLabel(self, value: tuple):
        self.__priceRangeInTicksLabel = value
        self._property_changed('priceRangeInTicksLabel')        

    @property
    def ticker(self) -> dict:
        return self.__ticker

    @ticker.setter
    def ticker(self, value: dict):
        self.__ticker = value
        self._property_changed('ticker')        

    @property
    def inRiskModel(self) -> dict:
        return self.__inRiskModel

    @inRiskModel.setter
    def inRiskModel(self, value: dict):
        self.__inRiskModel = value
        self._property_changed('inRiskModel')        

    @property
    def tcmCostHorizon1Day(self) -> dict:
        return self.__tcmCostHorizon1Day

    @tcmCostHorizon1Day.setter
    def tcmCostHorizon1Day(self, value: dict):
        self.__tcmCostHorizon1Day = value
        self._property_changed('tcmCostHorizon1Day')        

    @property
    def servicingCostLongPnl(self) -> dict:
        return self.__servicingCostLongPnl

    @servicingCostLongPnl.setter
    def servicingCostLongPnl(self, value: dict):
        self.__servicingCostLongPnl = value
        self._property_changed('servicingCostLongPnl')        

    @property
    def stsRatesCountry(self) -> dict:
        return self.__stsRatesCountry

    @stsRatesCountry.setter
    def stsRatesCountry(self, value: dict):
        self.__stsRatesCountry = value
        self._property_changed('stsRatesCountry')        

    @property
    def meetingNumber(self) -> dict:
        return self.__meetingNumber

    @meetingNumber.setter
    def meetingNumber(self, value: dict):
        self.__meetingNumber = value
        self._property_changed('meetingNumber')        

    @property
    def exchangeId(self) -> dict:
        return self.__exchangeId

    @exchangeId.setter
    def exchangeId(self, value: dict):
        self.__exchangeId = value
        self._property_changed('exchangeId')        

    @property
    def horizon(self) -> dict:
        return self.__horizon

    @horizon.setter
    def horizon(self, value: dict):
        self.__horizon = value
        self._property_changed('horizon')        

    @property
    def midGspread(self) -> dict:
        return self.__midGspread

    @midGspread.setter
    def midGspread(self, value: dict):
        self.__midGspread = value
        self._property_changed('midGspread')        

    @property
    def tcmCostHorizon20Day(self) -> dict:
        return self.__tcmCostHorizon20Day

    @tcmCostHorizon20Day.setter
    def tcmCostHorizon20Day(self, value: dict):
        self.__tcmCostHorizon20Day = value
        self._property_changed('tcmCostHorizon20Day')        

    @property
    def longLevel(self) -> dict:
        return self.__longLevel

    @longLevel.setter
    def longLevel(self, value: dict):
        self.__longLevel = value
        self._property_changed('longLevel')        

    @property
    def sourceValueForecast(self) -> dict:
        return self.__sourceValueForecast

    @sourceValueForecast.setter
    def sourceValueForecast(self, value: dict):
        self.__sourceValueForecast = value
        self._property_changed('sourceValueForecast')        

    @property
    def shortConvictionLarge(self) -> dict:
        return self.__shortConvictionLarge

    @shortConvictionLarge.setter
    def shortConvictionLarge(self, value: dict):
        self.__shortConvictionLarge = value
        self._property_changed('shortConvictionLarge')        

    @property
    def realm(self) -> dict:
        return self.__realm

    @realm.setter
    def realm(self, value: dict):
        self.__realm = value
        self._property_changed('realm')        

    @property
    def bid(self) -> dict:
        return self.__bid

    @bid.setter
    def bid(self, value: dict):
        self.__bid = value
        self._property_changed('bid')        

    @property
    def dataDescription(self) -> dict:
        return self.__dataDescription

    @dataDescription.setter
    def dataDescription(self, value: dict):
        self.__dataDescription = value
        self._property_changed('dataDescription')        

    @property
    def counterPartyStatus(self) -> dict:
        return self.__counterPartyStatus

    @counterPartyStatus.setter
    def counterPartyStatus(self, value: dict):
        self.__counterPartyStatus = value
        self._property_changed('counterPartyStatus')        

    @property
    def composite22DayAdv(self) -> dict:
        return self.__composite22DayAdv

    @composite22DayAdv.setter
    def composite22DayAdv(self, value: dict):
        self.__composite22DayAdv = value
        self._property_changed('composite22DayAdv')        

    @property
    def dollarExcessReturn(self) -> dict:
        return self.__dollarExcessReturn

    @dollarExcessReturn.setter
    def dollarExcessReturn(self, value: dict):
        self.__dollarExcessReturn = value
        self._property_changed('dollarExcessReturn')        

    @property
    def gsn(self) -> dict:
        return self.__gsn

    @gsn.setter
    def gsn(self, value: dict):
        self.__gsn = value
        self._property_changed('gsn')        

    @property
    def isAggressive(self) -> dict:
        return self.__isAggressive

    @isAggressive.setter
    def isAggressive(self, value: dict):
        self.__isAggressive = value
        self._property_changed('isAggressive')        

    @property
    def orderId(self) -> dict:
        return self.__orderId

    @orderId.setter
    def orderId(self, value: dict):
        self.__orderId = value
        self._property_changed('orderId')        

    @property
    def gss(self) -> dict:
        return self.__gss

    @gss.setter
    def gss(self, value: dict):
        self.__gss = value
        self._property_changed('gss')        

    @property
    def percentOfMediandv1m(self) -> dict:
        return self.__percentOfMediandv1m

    @percentOfMediandv1m.setter
    def percentOfMediandv1m(self, value: dict):
        self.__percentOfMediandv1m = value
        self._property_changed('percentOfMediandv1m')        

    @property
    def lendables(self) -> dict:
        return self.__lendables

    @lendables.setter
    def lendables(self, value: dict):
        self.__lendables = value
        self._property_changed('lendables')        

    @property
    def assetClass(self) -> dict:
        return self.__assetClass

    @assetClass.setter
    def assetClass(self, value: dict):
        self.__assetClass = value
        self._property_changed('assetClass')        

    @property
    def gsideid(self) -> dict:
        return self.__gsideid

    @gsideid.setter
    def gsideid(self, value: dict):
        self.__gsideid = value
        self._property_changed('gsideid')        

    @property
    def bosInTicksLabel(self) -> tuple:
        return self.__bosInTicksLabel

    @bosInTicksLabel.setter
    def bosInTicksLabel(self, value: tuple):
        self.__bosInTicksLabel = value
        self._property_changed('bosInTicksLabel')        

    @property
    def ric(self) -> dict:
        return self.__ric

    @ric.setter
    def ric(self, value: dict):
        self.__ric = value
        self._property_changed('ric')        

    @property
    def positionSourceId(self) -> dict:
        return self.__positionSourceId

    @positionSourceId.setter
    def positionSourceId(self, value: dict):
        self.__positionSourceId = value
        self._property_changed('positionSourceId')        

    @property
    def division(self) -> dict:
        return self.__division

    @division.setter
    def division(self, value: dict):
        self.__division = value
        self._property_changed('division')        

    @property
    def marketCapUSD(self) -> dict:
        return self.__marketCapUSD

    @marketCapUSD.setter
    def marketCapUSD(self, value: dict):
        self.__marketCapUSD = value
        self._property_changed('marketCapUSD')        

    @property
    def gsSustainRegion(self) -> dict:
        return self.__gsSustainRegion

    @gsSustainRegion.setter
    def gsSustainRegion(self, value: dict):
        self.__gsSustainRegion = value
        self._property_changed('gsSustainRegion')        

    @property
    def deploymentId(self) -> dict:
        return self.__deploymentId

    @deploymentId.setter
    def deploymentId(self, value: dict):
        self.__deploymentId = value
        self._property_changed('deploymentId')        

    @property
    def highPrice(self) -> dict:
        return self.__highPrice

    @highPrice.setter
    def highPrice(self, value: dict):
        self.__highPrice = value
        self._property_changed('highPrice')        

    @property
    def loanStatus(self) -> dict:
        return self.__loanStatus

    @loanStatus.setter
    def loanStatus(self, value: dict):
        self.__loanStatus = value
        self._property_changed('loanStatus')        

    @property
    def shortWeight(self) -> dict:
        return self.__shortWeight

    @shortWeight.setter
    def shortWeight(self, value: dict):
        self.__shortWeight = value
        self._property_changed('shortWeight')        

    @property
    def absoluteShares(self) -> dict:
        return self.__absoluteShares

    @absoluteShares.setter
    def absoluteShares(self, value: dict):
        self.__absoluteShares = value
        self._property_changed('absoluteShares')        

    @property
    def action(self) -> dict:
        return self.__action

    @action.setter
    def action(self, value: dict):
        self.__action = value
        self._property_changed('action')        

    @property
    def model(self) -> dict:
        return self.__model

    @model.setter
    def model(self, value: dict):
        self.__model = value
        self._property_changed('model')        

    @property
    def id(self) -> dict:
        return self.__id

    @id.setter
    def id(self, value: dict):
        self.__id = value
        self._property_changed('id')        

    @property
    def arrivalHaircutVwapNormalized(self) -> dict:
        return self.__arrivalHaircutVwapNormalized

    @arrivalHaircutVwapNormalized.setter
    def arrivalHaircutVwapNormalized(self, value: dict):
        self.__arrivalHaircutVwapNormalized = value
        self._property_changed('arrivalHaircutVwapNormalized')        

    @property
    def priceComponent(self) -> dict:
        return self.__priceComponent

    @priceComponent.setter
    def priceComponent(self, value: dict):
        self.__priceComponent = value
        self._property_changed('priceComponent')        

    @property
    def queueClockTimeDescription(self) -> dict:
        return self.__queueClockTimeDescription

    @queueClockTimeDescription.setter
    def queueClockTimeDescription(self, value: dict):
        self.__queueClockTimeDescription = value
        self._property_changed('queueClockTimeDescription')        

    @property
    def loanRebate(self) -> dict:
        return self.__loanRebate

    @loanRebate.setter
    def loanRebate(self, value: dict):
        self.__loanRebate = value
        self._property_changed('loanRebate')        

    @property
    def period(self) -> dict:
        return self.__period

    @period.setter
    def period(self, value: dict):
        self.__period = value
        self._property_changed('period')        

    @property
    def indexCreateSource(self) -> dict:
        return self.__indexCreateSource

    @indexCreateSource.setter
    def indexCreateSource(self, value: dict):
        self.__indexCreateSource = value
        self._property_changed('indexCreateSource')        

    @property
    def fiscalQuarter(self) -> dict:
        return self.__fiscalQuarter

    @fiscalQuarter.setter
    def fiscalQuarter(self, value: dict):
        self.__fiscalQuarter = value
        self._property_changed('fiscalQuarter')        

    @property
    def deltaStrike(self) -> dict:
        return self.__deltaStrike

    @deltaStrike.setter
    def deltaStrike(self, value: dict):
        self.__deltaStrike = value
        self._property_changed('deltaStrike')        

    @property
    def marketImpact(self) -> dict:
        return self.__marketImpact

    @marketImpact.setter
    def marketImpact(self, value: dict):
        self.__marketImpact = value
        self._property_changed('marketImpact')        

    @property
    def eventType(self) -> dict:
        return self.__eventType

    @eventType.setter
    def eventType(self, value: dict):
        self.__eventType = value
        self._property_changed('eventType')        

    @property
    def assetCountLong(self) -> dict:
        return self.__assetCountLong

    @assetCountLong.setter
    def assetCountLong(self, value: dict):
        self.__assetCountLong = value
        self._property_changed('assetCountLong')        

    @property
    def valueActual(self) -> dict:
        return self.__valueActual

    @valueActual.setter
    def valueActual(self, value: dict):
        self.__valueActual = value
        self._property_changed('valueActual')        

    @property
    def bcid(self) -> dict:
        return self.__bcid

    @bcid.setter
    def bcid(self, value: dict):
        self.__bcid = value
        self._property_changed('bcid')        

    @property
    def collateralCurrency(self) -> dict:
        return self.__collateralCurrency

    @collateralCurrency.setter
    def collateralCurrency(self, value: dict):
        self.__collateralCurrency = value
        self._property_changed('collateralCurrency')        

    @property
    def originalCountry(self) -> dict:
        return self.__originalCountry

    @originalCountry.setter
    def originalCountry(self, value: dict):
        self.__originalCountry = value
        self._property_changed('originalCountry')        

    @property
    def touchLiquidityScore(self) -> dict:
        return self.__touchLiquidityScore

    @touchLiquidityScore.setter
    def touchLiquidityScore(self, value: dict):
        self.__touchLiquidityScore = value
        self._property_changed('touchLiquidityScore')        

    @property
    def field(self) -> dict:
        return self.__field

    @field.setter
    def field(self, value: dict):
        self.__field = value
        self._property_changed('field')        

    @property
    def factorCategoryId(self) -> dict:
        return self.__factorCategoryId

    @factorCategoryId.setter
    def factorCategoryId(self, value: dict):
        self.__factorCategoryId = value
        self._property_changed('factorCategoryId')        

    @property
    def spot(self) -> dict:
        return self.__spot

    @spot.setter
    def spot(self, value: dict):
        self.__spot = value
        self._property_changed('spot')        

    @property
    def expectedCompletionDate(self) -> dict:
        return self.__expectedCompletionDate

    @expectedCompletionDate.setter
    def expectedCompletionDate(self, value: dict):
        self.__expectedCompletionDate = value
        self._property_changed('expectedCompletionDate')        

    @property
    def loanValue(self) -> dict:
        return self.__loanValue

    @loanValue.setter
    def loanValue(self, value: dict):
        self.__loanValue = value
        self._property_changed('loanValue')        

    @property
    def tradingRestriction(self) -> dict:
        return self.__tradingRestriction

    @tradingRestriction.setter
    def tradingRestriction(self, value: dict):
        self.__tradingRestriction = value
        self._property_changed('tradingRestriction')        

    @property
    def skew(self) -> dict:
        return self.__skew

    @skew.setter
    def skew(self, value: dict):
        self.__skew = value
        self._property_changed('skew')        

    @property
    def status(self) -> dict:
        return self.__status

    @status.setter
    def status(self, value: dict):
        self.__status = value
        self._property_changed('status')        

    @property
    def sustainEmergingMarkets(self) -> dict:
        return self.__sustainEmergingMarkets

    @sustainEmergingMarkets.setter
    def sustainEmergingMarkets(self, value: dict):
        self.__sustainEmergingMarkets = value
        self._property_changed('sustainEmergingMarkets')        

    @property
    def totalReturnPrice(self) -> dict:
        return self.__totalReturnPrice

    @totalReturnPrice.setter
    def totalReturnPrice(self, value: dict):
        self.__totalReturnPrice = value
        self._property_changed('totalReturnPrice')        

    @property
    def city(self) -> dict:
        return self.__city

    @city.setter
    def city(self, value: dict):
        self.__city = value
        self._property_changed('city')        

    @property
    def totalPrice(self) -> dict:
        return self.__totalPrice

    @totalPrice.setter
    def totalPrice(self, value: dict):
        self.__totalPrice = value
        self._property_changed('totalPrice')        

    @property
    def eventSource(self) -> dict:
        return self.__eventSource

    @eventSource.setter
    def eventSource(self, value: dict):
        self.__eventSource = value
        self._property_changed('eventSource')        

    @property
    def qisPermNo(self) -> dict:
        return self.__qisPermNo

    @qisPermNo.setter
    def qisPermNo(self, value: dict):
        self.__qisPermNo = value
        self._property_changed('qisPermNo')        

    @property
    def hitRateYtd(self) -> dict:
        return self.__hitRateYtd

    @hitRateYtd.setter
    def hitRateYtd(self, value: dict):
        self.__hitRateYtd = value
        self._property_changed('hitRateYtd')        

    @property
    def valid(self) -> dict:
        return self.__valid

    @valid.setter
    def valid(self, value: dict):
        self.__valid = value
        self._property_changed('valid')        

    @property
    def stsCommodity(self) -> dict:
        return self.__stsCommodity

    @stsCommodity.setter
    def stsCommodity(self, value: dict):
        self.__stsCommodity = value
        self._property_changed('stsCommodity')        

    @property
    def stsCommoditySector(self) -> dict:
        return self.__stsCommoditySector

    @stsCommoditySector.setter
    def stsCommoditySector(self, value: dict):
        self.__stsCommoditySector = value
        self._property_changed('stsCommoditySector')        

    @property
    def exceptionStatus(self) -> dict:
        return self.__exceptionStatus

    @exceptionStatus.setter
    def exceptionStatus(self, value: dict):
        self.__exceptionStatus = value
        self._property_changed('exceptionStatus')        

    @property
    def salesCoverage(self) -> dict:
        return self.__salesCoverage

    @salesCoverage.setter
    def salesCoverage(self, value: dict):
        self.__salesCoverage = value
        self._property_changed('salesCoverage')        

    @property
    def shortExposure(self) -> dict:
        return self.__shortExposure

    @shortExposure.setter
    def shortExposure(self, value: dict):
        self.__shortExposure = value
        self._property_changed('shortExposure')        

    @property
    def esScore(self) -> dict:
        return self.__esScore

    @esScore.setter
    def esScore(self, value: dict):
        self.__esScore = value
        self._property_changed('esScore')        

    @property
    def tcmCostParticipationRate10Pct(self) -> dict:
        return self.__tcmCostParticipationRate10Pct

    @tcmCostParticipationRate10Pct.setter
    def tcmCostParticipationRate10Pct(self, value: dict):
        self.__tcmCostParticipationRate10Pct = value
        self._property_changed('tcmCostParticipationRate10Pct')        

    @property
    def eventTime(self) -> dict:
        return self.__eventTime

    @eventTime.setter
    def eventTime(self, value: dict):
        self.__eventTime = value
        self._property_changed('eventTime')        

    @property
    def positionSourceName(self) -> dict:
        return self.__positionSourceName

    @positionSourceName.setter
    def positionSourceName(self, value: dict):
        self.__positionSourceName = value
        self._property_changed('positionSourceName')        

    @property
    def priceRangeInTicks(self) -> dict:
        return self.__priceRangeInTicks

    @priceRangeInTicks.setter
    def priceRangeInTicks(self, value: dict):
        self.__priceRangeInTicks = value
        self._property_changed('priceRangeInTicks')        

    @property
    def arrivalHaircutVwap(self) -> dict:
        return self.__arrivalHaircutVwap

    @arrivalHaircutVwap.setter
    def arrivalHaircutVwap(self, value: dict):
        self.__arrivalHaircutVwap = value
        self._property_changed('arrivalHaircutVwap')        

    @property
    def interestRate(self) -> dict:
        return self.__interestRate

    @interestRate.setter
    def interestRate(self, value: dict):
        self.__interestRate = value
        self._property_changed('interestRate')        

    @property
    def executionDays(self) -> dict:
        return self.__executionDays

    @executionDays.setter
    def executionDays(self, value: dict):
        self.__executionDays = value
        self._property_changed('executionDays')        

    @property
    def pctChange(self) -> dict:
        return self.__pctChange

    @pctChange.setter
    def pctChange(self, value: dict):
        self.__pctChange = value
        self._property_changed('pctChange')        

    @property
    def side(self) -> dict:
        return self.__side

    @side.setter
    def side(self, value: dict):
        self.__side = value
        self._property_changed('side')        

    @property
    def numberOfRolls(self) -> dict:
        return self.__numberOfRolls

    @numberOfRolls.setter
    def numberOfRolls(self, value: dict):
        self.__numberOfRolls = value
        self._property_changed('numberOfRolls')        

    @property
    def agentLenderFee(self) -> dict:
        return self.__agentLenderFee

    @agentLenderFee.setter
    def agentLenderFee(self, value: dict):
        self.__agentLenderFee = value
        self._property_changed('agentLenderFee')        

    @property
    def complianceRestrictedStatus(self) -> dict:
        return self.__complianceRestrictedStatus

    @complianceRestrictedStatus.setter
    def complianceRestrictedStatus(self, value: dict):
        self.__complianceRestrictedStatus = value
        self._property_changed('complianceRestrictedStatus')        

    @property
    def forward(self) -> dict:
        return self.__forward

    @forward.setter
    def forward(self, value: dict):
        self.__forward = value
        self._property_changed('forward')        

    @property
    def borrowFee(self) -> dict:
        return self.__borrowFee

    @borrowFee.setter
    def borrowFee(self, value: dict):
        self.__borrowFee = value
        self._property_changed('borrowFee')        

    @property
    def strike(self) -> dict:
        return self.__strike

    @strike.setter
    def strike(self, value: dict):
        self.__strike = value
        self._property_changed('strike')        

    @property
    def loanSpread(self) -> dict:
        return self.__loanSpread

    @loanSpread.setter
    def loanSpread(self, value: dict):
        self.__loanSpread = value
        self._property_changed('loanSpread')        

    @property
    def tcmCostHorizon12Hour(self) -> dict:
        return self.__tcmCostHorizon12Hour

    @tcmCostHorizon12Hour.setter
    def tcmCostHorizon12Hour(self, value: dict):
        self.__tcmCostHorizon12Hour = value
        self._property_changed('tcmCostHorizon12Hour')        

    @property
    def dewPoint(self) -> dict:
        return self.__dewPoint

    @dewPoint.setter
    def dewPoint(self, value: dict):
        self.__dewPoint = value
        self._property_changed('dewPoint')        

    @property
    def researchCommission(self) -> dict:
        return self.__researchCommission

    @researchCommission.setter
    def researchCommission(self, value: dict):
        self.__researchCommission = value
        self._property_changed('researchCommission')        

    @property
    def bbid(self) -> dict:
        return self.__bbid

    @bbid.setter
    def bbid(self, value: dict):
        self.__bbid = value
        self._property_changed('bbid')        

    @property
    def assetClassificationsRiskCountryCode(self) -> dict:
        return self.__assetClassificationsRiskCountryCode

    @assetClassificationsRiskCountryCode.setter
    def assetClassificationsRiskCountryCode(self, value: dict):
        self.__assetClassificationsRiskCountryCode = value
        self._property_changed('assetClassificationsRiskCountryCode')        

    @property
    def eventStatus(self) -> dict:
        return self.__eventStatus

    @eventStatus.setter
    def eventStatus(self, value: dict):
        self.__eventStatus = value
        self._property_changed('eventStatus')        

    @property
    def return_(self) -> dict:
        return self.__return

    @return_.setter
    def return_(self, value: dict):
        self.__return = value
        self._property_changed('return')        

    @property
    def maxTemperature(self) -> dict:
        return self.__maxTemperature

    @maxTemperature.setter
    def maxTemperature(self, value: dict):
        self.__maxTemperature = value
        self._property_changed('maxTemperature')        

    @property
    def acquirerShareholderMeetingDate(self) -> dict:
        return self.__acquirerShareholderMeetingDate

    @acquirerShareholderMeetingDate.setter
    def acquirerShareholderMeetingDate(self, value: dict):
        self.__acquirerShareholderMeetingDate = value
        self._property_changed('acquirerShareholderMeetingDate')        

    @property
    def arrivalMidNormalized(self) -> dict:
        return self.__arrivalMidNormalized

    @arrivalMidNormalized.setter
    def arrivalMidNormalized(self, value: dict):
        self.__arrivalMidNormalized = value
        self._property_changed('arrivalMidNormalized')        

    @property
    def rating(self) -> dict:
        return self.__rating

    @rating.setter
    def rating(self, value: dict):
        self.__rating = value
        self._property_changed('rating')        

    @property
    def volatility(self) -> dict:
        return self.__volatility

    @volatility.setter
    def volatility(self, value: dict):
        self.__volatility = value
        self._property_changed('volatility')        

    @property
    def arrivalRtNormalized(self) -> dict:
        return self.__arrivalRtNormalized

    @arrivalRtNormalized.setter
    def arrivalRtNormalized(self, value: dict):
        self.__arrivalRtNormalized = value
        self._property_changed('arrivalRtNormalized')        

    @property
    def performanceFee(self) -> dict:
        return self.__performanceFee

    @performanceFee.setter
    def performanceFee(self, value: dict):
        self.__performanceFee = value
        self._property_changed('performanceFee')        

    @property
    def reportType(self) -> dict:
        return self.__reportType

    @reportType.setter
    def reportType(self, value: dict):
        self.__reportType = value
        self._property_changed('reportType')        

    @property
    def sourceURL(self) -> dict:
        return self.__sourceURL

    @sourceURL.setter
    def sourceURL(self, value: dict):
        self.__sourceURL = value
        self._property_changed('sourceURL')        

    @property
    def estimatedReturn(self) -> dict:
        return self.__estimatedReturn

    @estimatedReturn.setter
    def estimatedReturn(self, value: dict):
        self.__estimatedReturn = value
        self._property_changed('estimatedReturn')        

    @property
    def underlyingAssetIds(self) -> dict:
        return self.__underlyingAssetIds

    @underlyingAssetIds.setter
    def underlyingAssetIds(self, value: dict):
        self.__underlyingAssetIds = value
        self._property_changed('underlyingAssetIds')        

    @property
    def high(self) -> dict:
        return self.__high

    @high.setter
    def high(self, value: dict):
        self.__high = value
        self._property_changed('high')        

    @property
    def sourceLastUpdate(self) -> dict:
        return self.__sourceLastUpdate

    @sourceLastUpdate.setter
    def sourceLastUpdate(self, value: dict):
        self.__sourceLastUpdate = value
        self._property_changed('sourceLastUpdate')        

    @property
    def queueInLotsLabel(self) -> tuple:
        return self.__queueInLotsLabel

    @queueInLotsLabel.setter
    def queueInLotsLabel(self, value: tuple):
        self.__queueInLotsLabel = value
        self._property_changed('queueInLotsLabel')        

    @property
    def adv10DayPct(self) -> dict:
        return self.__adv10DayPct

    @adv10DayPct.setter
    def adv10DayPct(self, value: dict):
        self.__adv10DayPct = value
        self._property_changed('adv10DayPct')        

    @property
    def longConvictionMedium(self) -> dict:
        return self.__longConvictionMedium

    @longConvictionMedium.setter
    def longConvictionMedium(self, value: dict):
        self.__longConvictionMedium = value
        self._property_changed('longConvictionMedium')        

    @property
    def eventName(self) -> dict:
        return self.__eventName

    @eventName.setter
    def eventName(self, value: dict):
        self.__eventName = value
        self._property_changed('eventName')        

    @property
    def annualRisk(self) -> dict:
        return self.__annualRisk

    @annualRisk.setter
    def annualRisk(self, value: dict):
        self.__annualRisk = value
        self._property_changed('annualRisk')        

    @property
    def eti(self) -> dict:
        return self.__eti

    @eti.setter
    def eti(self, value: dict):
        self.__eti = value
        self._property_changed('eti')        

    @property
    def dailyTrackingError(self) -> dict:
        return self.__dailyTrackingError

    @dailyTrackingError.setter
    def dailyTrackingError(self, value: dict):
        self.__dailyTrackingError = value
        self._property_changed('dailyTrackingError')        

    @property
    def unadjustedBid(self) -> dict:
        return self.__unadjustedBid

    @unadjustedBid.setter
    def unadjustedBid(self, value: dict):
        self.__unadjustedBid = value
        self._property_changed('unadjustedBid')        

    @property
    def gsdeer(self) -> dict:
        return self.__gsdeer

    @gsdeer.setter
    def gsdeer(self, value: dict):
        self.__gsdeer = value
        self._property_changed('gsdeer')        

    @property
    def gRegionalPercentile(self) -> dict:
        return self.__gRegionalPercentile

    @gRegionalPercentile.setter
    def gRegionalPercentile(self, value: dict):
        self.__gRegionalPercentile = value
        self._property_changed('gRegionalPercentile')        

    @property
    def marketBuffer(self) -> dict:
        return self.__marketBuffer

    @marketBuffer.setter
    def marketBuffer(self, value: dict):
        self.__marketBuffer = value
        self._property_changed('marketBuffer')        

    @property
    def marketCap(self) -> dict:
        return self.__marketCap

    @marketCap.setter
    def marketCap(self, value: dict):
        self.__marketCap = value
        self._property_changed('marketCap')        

    @property
    def oeId(self) -> dict:
        return self.__oeId

    @oeId.setter
    def oeId(self, value: dict):
        self.__oeId = value
        self._property_changed('oeId')        

    @property
    def clusterRegion(self) -> tuple:
        return self.__clusterRegion

    @clusterRegion.setter
    def clusterRegion(self, value: tuple):
        self.__clusterRegion = value
        self._property_changed('clusterRegion')        

    @property
    def bbidEquivalent(self) -> dict:
        return self.__bbidEquivalent

    @bbidEquivalent.setter
    def bbidEquivalent(self, value: dict):
        self.__bbidEquivalent = value
        self._property_changed('bbidEquivalent')        

    @property
    def prevCloseAsk(self) -> dict:
        return self.__prevCloseAsk

    @prevCloseAsk.setter
    def prevCloseAsk(self, value: dict):
        self.__prevCloseAsk = value
        self._property_changed('prevCloseAsk')        

    @property
    def level(self) -> dict:
        return self.__level

    @level.setter
    def level(self, value: dict):
        self.__level = value
        self._property_changed('level')        

    @property
    def valoren(self) -> dict:
        return self.__valoren

    @valoren.setter
    def valoren(self, value: dict):
        self.__valoren = value
        self._property_changed('valoren')        

    @property
    def esMomentumScore(self) -> dict:
        return self.__esMomentumScore

    @esMomentumScore.setter
    def esMomentumScore(self, value: dict):
        self.__esMomentumScore = value
        self._property_changed('esMomentumScore')        

    @property
    def pressure(self) -> dict:
        return self.__pressure

    @pressure.setter
    def pressure(self, value: dict):
        self.__pressure = value
        self._property_changed('pressure')        

    @property
    def shortDescription(self) -> dict:
        return self.__shortDescription

    @shortDescription.setter
    def shortDescription(self, value: dict):
        self.__shortDescription = value
        self._property_changed('shortDescription')        

    @property
    def basis(self) -> dict:
        return self.__basis

    @basis.setter
    def basis(self, value: dict):
        self.__basis = value
        self._property_changed('basis')        

    @property
    def netWeight(self) -> dict:
        return self.__netWeight

    @netWeight.setter
    def netWeight(self, value: dict):
        self.__netWeight = value
        self._property_changed('netWeight')        

    @property
    def hedgeId(self) -> dict:
        return self.__hedgeId

    @hedgeId.setter
    def hedgeId(self, value: dict):
        self.__hedgeId = value
        self._property_changed('hedgeId')        

    @property
    def portfolioManagers(self) -> dict:
        return self.__portfolioManagers

    @portfolioManagers.setter
    def portfolioManagers(self, value: dict):
        self.__portfolioManagers = value
        self._property_changed('portfolioManagers')        

    @property
    def assetParametersCommoditySector(self) -> dict:
        return self.__assetParametersCommoditySector

    @assetParametersCommoditySector.setter
    def assetParametersCommoditySector(self, value: dict):
        self.__assetParametersCommoditySector = value
        self._property_changed('assetParametersCommoditySector')        

    @property
    def bosInTicks(self) -> dict:
        return self.__bosInTicks

    @bosInTicks.setter
    def bosInTicks(self, value: dict):
        self.__bosInTicks = value
        self._property_changed('bosInTicks')        

    @property
    def tcmCostHorizon8Day(self) -> dict:
        return self.__tcmCostHorizon8Day

    @tcmCostHorizon8Day.setter
    def tcmCostHorizon8Day(self, value: dict):
        self.__tcmCostHorizon8Day = value
        self._property_changed('tcmCostHorizon8Day')        

    @property
    def supraStrategy(self) -> dict:
        return self.__supraStrategy

    @supraStrategy.setter
    def supraStrategy(self, value: dict):
        self.__supraStrategy = value
        self._property_changed('supraStrategy')        

    @property
    def marketBufferThreshold(self) -> dict:
        return self.__marketBufferThreshold

    @marketBufferThreshold.setter
    def marketBufferThreshold(self, value: dict):
        self.__marketBufferThreshold = value
        self._property_changed('marketBufferThreshold')        

    @property
    def adv5DayPct(self) -> dict:
        return self.__adv5DayPct

    @adv5DayPct.setter
    def adv5DayPct(self, value: dict):
        self.__adv5DayPct = value
        self._property_changed('adv5DayPct')        

    @property
    def factorSource(self) -> dict:
        return self.__factorSource

    @factorSource.setter
    def factorSource(self, value: dict):
        self.__factorSource = value
        self._property_changed('factorSource')        

    @property
    def leverage(self) -> dict:
        return self.__leverage

    @leverage.setter
    def leverage(self, value: dict):
        self.__leverage = value
        self._property_changed('leverage')        

    @property
    def submitter(self) -> dict:
        return self.__submitter

    @submitter.setter
    def submitter(self, value: dict):
        self.__submitter = value
        self._property_changed('submitter')        

    @property
    def notional(self) -> dict:
        return self.__notional

    @notional.setter
    def notional(self, value: dict):
        self.__notional = value
        self._property_changed('notional')        

    @property
    def esDisclosurePercentage(self) -> dict:
        return self.__esDisclosurePercentage

    @esDisclosurePercentage.setter
    def esDisclosurePercentage(self, value: dict):
        self.__esDisclosurePercentage = value
        self._property_changed('esDisclosurePercentage')        

    @property
    def investmentIncome(self) -> dict:
        return self.__investmentIncome

    @investmentIncome.setter
    def investmentIncome(self, value: dict):
        self.__investmentIncome = value
        self._property_changed('investmentIncome')        

    @property
    def clientShortName(self) -> dict:
        return self.__clientShortName

    @clientShortName.setter
    def clientShortName(self, value: dict):
        self.__clientShortName = value
        self._property_changed('clientShortName')        

    @property
    def fwdPoints(self) -> dict:
        return self.__fwdPoints

    @fwdPoints.setter
    def fwdPoints(self, value: dict):
        self.__fwdPoints = value
        self._property_changed('fwdPoints')        

    @property
    def groupCategory(self) -> dict:
        return self.__groupCategory

    @groupCategory.setter
    def groupCategory(self, value: dict):
        self.__groupCategory = value
        self._property_changed('groupCategory')        

    @property
    def kpiId(self) -> dict:
        return self.__kpiId

    @kpiId.setter
    def kpiId(self, value: dict):
        self.__kpiId = value
        self._property_changed('kpiId')        

    @property
    def relativeReturnWtd(self) -> dict:
        return self.__relativeReturnWtd

    @relativeReturnWtd.setter
    def relativeReturnWtd(self, value: dict):
        self.__relativeReturnWtd = value
        self._property_changed('relativeReturnWtd')        

    @property
    def bidPlusAsk(self) -> dict:
        return self.__bidPlusAsk

    @bidPlusAsk.setter
    def bidPlusAsk(self, value: dict):
        self.__bidPlusAsk = value
        self._property_changed('bidPlusAsk')        

    @property
    def borrowCost(self) -> dict:
        return self.__borrowCost

    @borrowCost.setter
    def borrowCost(self, value: dict):
        self.__borrowCost = value
        self._property_changed('borrowCost')        

    @property
    def assetClassificationsRiskCountryName(self) -> dict:
        return self.__assetClassificationsRiskCountryName

    @assetClassificationsRiskCountryName.setter
    def assetClassificationsRiskCountryName(self, value: dict):
        self.__assetClassificationsRiskCountryName = value
        self._property_changed('assetClassificationsRiskCountryName')        

    @property
    def total(self) -> dict:
        return self.__total

    @total.setter
    def total(self, value: dict):
        self.__total = value
        self._property_changed('total')        

    @property
    def riskModel(self) -> dict:
        return self.__riskModel

    @riskModel.setter
    def riskModel(self, value: dict):
        self.__riskModel = value
        self._property_changed('riskModel')        

    @property
    def assetId(self) -> dict:
        return self.__assetId

    @assetId.setter
    def assetId(self, value: dict):
        self.__assetId = value
        self._property_changed('assetId')        

    @property
    def averageImpliedVolatility(self) -> dict:
        return self.__averageImpliedVolatility

    @averageImpliedVolatility.setter
    def averageImpliedVolatility(self, value: dict):
        self.__averageImpliedVolatility = value
        self._property_changed('averageImpliedVolatility')        

    @property
    def fairValue(self) -> dict:
        return self.__fairValue

    @fairValue.setter
    def fairValue(self, value: dict):
        self.__fairValue = value
        self._property_changed('fairValue')        

    @property
    def adjustedHighPrice(self) -> dict:
        return self.__adjustedHighPrice

    @adjustedHighPrice.setter
    def adjustedHighPrice(self, value: dict):
        self.__adjustedHighPrice = value
        self._property_changed('adjustedHighPrice')        

    @property
    def beta(self) -> dict:
        return self.__beta

    @beta.setter
    def beta(self, value: dict):
        self.__beta = value
        self._property_changed('beta')        

    @property
    def direction(self) -> dict:
        return self.__direction

    @direction.setter
    def direction(self, value: dict):
        self.__direction = value
        self._property_changed('direction')        

    @property
    def valueForecast(self) -> dict:
        return self.__valueForecast

    @valueForecast.setter
    def valueForecast(self, value: dict):
        self.__valueForecast = value
        self._property_changed('valueForecast')        

    @property
    def longExposure(self) -> dict:
        return self.__longExposure

    @longExposure.setter
    def longExposure(self, value: dict):
        self.__longExposure = value
        self._property_changed('longExposure')        

    @property
    def positionSourceType(self) -> dict:
        return self.__positionSourceType

    @positionSourceType.setter
    def positionSourceType(self, value: dict):
        self.__positionSourceType = value
        self._property_changed('positionSourceType')        

    @property
    def tcmCostParticipationRate20Pct(self) -> dict:
        return self.__tcmCostParticipationRate20Pct

    @tcmCostParticipationRate20Pct.setter
    def tcmCostParticipationRate20Pct(self, value: dict):
        self.__tcmCostParticipationRate20Pct = value
        self._property_changed('tcmCostParticipationRate20Pct')        

    @property
    def adjustedClosePrice(self) -> dict:
        return self.__adjustedClosePrice

    @adjustedClosePrice.setter
    def adjustedClosePrice(self, value: dict):
        self.__adjustedClosePrice = value
        self._property_changed('adjustedClosePrice')        

    @property
    def cross(self) -> dict:
        return self.__cross

    @cross.setter
    def cross(self, value: dict):
        self.__cross = value
        self._property_changed('cross')        

    @property
    def lmsId(self) -> dict:
        return self.__lmsId

    @lmsId.setter
    def lmsId(self, value: dict):
        self.__lmsId = value
        self._property_changed('lmsId')        

    @property
    def rebateRate(self) -> dict:
        return self.__rebateRate

    @rebateRate.setter
    def rebateRate(self, value: dict):
        self.__rebateRate = value
        self._property_changed('rebateRate')        

    @property
    def ideaStatus(self) -> dict:
        return self.__ideaStatus

    @ideaStatus.setter
    def ideaStatus(self, value: dict):
        self.__ideaStatus = value
        self._property_changed('ideaStatus')        

    @property
    def participationRate(self) -> dict:
        return self.__participationRate

    @participationRate.setter
    def participationRate(self, value: dict):
        self.__participationRate = value
        self._property_changed('participationRate')        

    @property
    def obfr(self) -> dict:
        return self.__obfr

    @obfr.setter
    def obfr(self, value: dict):
        self.__obfr = value
        self._property_changed('obfr')        

    @property
    def fxForecast(self) -> dict:
        return self.__fxForecast

    @fxForecast.setter
    def fxForecast(self, value: dict):
        self.__fxForecast = value
        self._property_changed('fxForecast')        

    @property
    def fixingTimeLabel(self) -> dict:
        return self.__fixingTimeLabel

    @fixingTimeLabel.setter
    def fixingTimeLabel(self, value: dict):
        self.__fixingTimeLabel = value
        self._property_changed('fixingTimeLabel')        

    @property
    def implementationId(self) -> dict:
        return self.__implementationId

    @implementationId.setter
    def implementationId(self, value: dict):
        self.__implementationId = value
        self._property_changed('implementationId')        

    @property
    def fillId(self) -> dict:
        return self.__fillId

    @fillId.setter
    def fillId(self, value: dict):
        self.__fillId = value
        self._property_changed('fillId')        

    @property
    def excessReturns(self) -> dict:
        return self.__excessReturns

    @excessReturns.setter
    def excessReturns(self, value: dict):
        self.__excessReturns = value
        self._property_changed('excessReturns')        

    @property
    def esMomentumPercentile(self) -> dict:
        return self.__esMomentumPercentile

    @esMomentumPercentile.setter
    def esMomentumPercentile(self, value: dict):
        self.__esMomentumPercentile = value
        self._property_changed('esMomentumPercentile')        

    @property
    def dollarReturn(self) -> dict:
        return self.__dollarReturn

    @dollarReturn.setter
    def dollarReturn(self, value: dict):
        self.__dollarReturn = value
        self._property_changed('dollarReturn')        

    @property
    def esNumericScore(self) -> dict:
        return self.__esNumericScore

    @esNumericScore.setter
    def esNumericScore(self, value: dict):
        self.__esNumericScore = value
        self._property_changed('esNumericScore')        

    @property
    def lenderIncomeAdjustment(self) -> dict:
        return self.__lenderIncomeAdjustment

    @lenderIncomeAdjustment.setter
    def lenderIncomeAdjustment(self, value: dict):
        self.__lenderIncomeAdjustment = value
        self._property_changed('lenderIncomeAdjustment')        

    @property
    def inBenchmark(self) -> dict:
        return self.__inBenchmark

    @inBenchmark.setter
    def inBenchmark(self, value: dict):
        self.__inBenchmark = value
        self._property_changed('inBenchmark')        

    @property
    def strategy(self) -> dict:
        return self.__strategy

    @strategy.setter
    def strategy(self, value: dict):
        self.__strategy = value
        self._property_changed('strategy')        

    @property
    def positionType(self) -> dict:
        return self.__positionType

    @positionType.setter
    def positionType(self, value: dict):
        self.__positionType = value
        self._property_changed('positionType')        

    @property
    def lenderIncome(self) -> dict:
        return self.__lenderIncome

    @lenderIncome.setter
    def lenderIncome(self, value: dict):
        self.__lenderIncome = value
        self._property_changed('lenderIncome')        

    @property
    def shortInterest(self) -> dict:
        return self.__shortInterest

    @shortInterest.setter
    def shortInterest(self, value: dict):
        self.__shortInterest = value
        self._property_changed('shortInterest')        

    @property
    def referencePeriod(self) -> dict:
        return self.__referencePeriod

    @referencePeriod.setter
    def referencePeriod(self, value: dict):
        self.__referencePeriod = value
        self._property_changed('referencePeriod')        

    @property
    def adjustedVolume(self) -> dict:
        return self.__adjustedVolume

    @adjustedVolume.setter
    def adjustedVolume(self, value: dict):
        self.__adjustedVolume = value
        self._property_changed('adjustedVolume')        

    @property
    def queueInLotsDescription(self) -> dict:
        return self.__queueInLotsDescription

    @queueInLotsDescription.setter
    def queueInLotsDescription(self, value: dict):
        self.__queueInLotsDescription = value
        self._property_changed('queueInLotsDescription')        

    @property
    def pbClientId(self) -> dict:
        return self.__pbClientId

    @pbClientId.setter
    def pbClientId(self, value: dict):
        self.__pbClientId = value
        self._property_changed('pbClientId')        

    @property
    def ownerId(self) -> dict:
        return self.__ownerId

    @ownerId.setter
    def ownerId(self, value: dict):
        self.__ownerId = value
        self._property_changed('ownerId')        

    @property
    def secDB(self) -> dict:
        return self.__secDB

    @secDB.setter
    def secDB(self, value: dict):
        self.__secDB = value
        self._property_changed('secDB')        

    @property
    def composite10DayAdv(self) -> dict:
        return self.__composite10DayAdv

    @composite10DayAdv.setter
    def composite10DayAdv(self, value: dict):
        self.__composite10DayAdv = value
        self._property_changed('composite10DayAdv')        

    @property
    def objective(self) -> dict:
        return self.__objective

    @objective.setter
    def objective(self, value: dict):
        self.__objective = value
        self._property_changed('objective')        

    @property
    def bpeQualityStars(self) -> dict:
        return self.__bpeQualityStars

    @bpeQualityStars.setter
    def bpeQualityStars(self, value: dict):
        self.__bpeQualityStars = value
        self._property_changed('bpeQualityStars')        

    @property
    def navPrice(self) -> dict:
        return self.__navPrice

    @navPrice.setter
    def navPrice(self, value: dict):
        self.__navPrice = value
        self._property_changed('navPrice')        

    @property
    def ideaActivityType(self) -> dict:
        return self.__ideaActivityType

    @ideaActivityType.setter
    def ideaActivityType(self, value: dict):
        self.__ideaActivityType = value
        self._property_changed('ideaActivityType')        

    @property
    def precipitation(self) -> dict:
        return self.__precipitation

    @precipitation.setter
    def precipitation(self, value: dict):
        self.__precipitation = value
        self._property_changed('precipitation')        

    @property
    def ideaSource(self) -> dict:
        return self.__ideaSource

    @ideaSource.setter
    def ideaSource(self, value: dict):
        self.__ideaSource = value
        self._property_changed('ideaSource')        

    @property
    def hedgeNotional(self) -> dict:
        return self.__hedgeNotional

    @hedgeNotional.setter
    def hedgeNotional(self, value: dict):
        self.__hedgeNotional = value
        self._property_changed('hedgeNotional')        

    @property
    def askLow(self) -> dict:
        return self.__askLow

    @askLow.setter
    def askLow(self, value: dict):
        self.__askLow = value
        self._property_changed('askLow')        

    @property
    def unadjustedAsk(self) -> dict:
        return self.__unadjustedAsk

    @unadjustedAsk.setter
    def unadjustedAsk(self, value: dict):
        self.__unadjustedAsk = value
        self._property_changed('unadjustedAsk')        

    @property
    def betaAdjustedNetExposure(self) -> dict:
        return self.__betaAdjustedNetExposure

    @betaAdjustedNetExposure.setter
    def betaAdjustedNetExposure(self, value: dict):
        self.__betaAdjustedNetExposure = value
        self._property_changed('betaAdjustedNetExposure')        

    @property
    def expiry(self) -> dict:
        return self.__expiry

    @expiry.setter
    def expiry(self, value: dict):
        self.__expiry = value
        self._property_changed('expiry')        

    @property
    def tradingPnl(self) -> dict:
        return self.__tradingPnl

    @tradingPnl.setter
    def tradingPnl(self, value: dict):
        self.__tradingPnl = value
        self._property_changed('tradingPnl')        

    @property
    def strikePercentage(self) -> dict:
        return self.__strikePercentage

    @strikePercentage.setter
    def strikePercentage(self, value: dict):
        self.__strikePercentage = value
        self._property_changed('strikePercentage')        

    @property
    def excessReturnPrice(self) -> dict:
        return self.__excessReturnPrice

    @excessReturnPrice.setter
    def excessReturnPrice(self, value: dict):
        self.__excessReturnPrice = value
        self._property_changed('excessReturnPrice')        

    @property
    def givenPlusPaid(self) -> dict:
        return self.__givenPlusPaid

    @givenPlusPaid.setter
    def givenPlusPaid(self, value: dict):
        self.__givenPlusPaid = value
        self._property_changed('givenPlusPaid')        

    @property
    def shortConvictionSmall(self) -> dict:
        return self.__shortConvictionSmall

    @shortConvictionSmall.setter
    def shortConvictionSmall(self, value: dict):
        self.__shortConvictionSmall = value
        self._property_changed('shortConvictionSmall')        

    @property
    def prevCloseBid(self) -> dict:
        return self.__prevCloseBid

    @prevCloseBid.setter
    def prevCloseBid(self, value: dict):
        self.__prevCloseBid = value
        self._property_changed('prevCloseBid')        

    @property
    def fxPnl(self) -> dict:
        return self.__fxPnl

    @fxPnl.setter
    def fxPnl(self, value: dict):
        self.__fxPnl = value
        self._property_changed('fxPnl')        

    @property
    def forecast(self) -> dict:
        return self.__forecast

    @forecast.setter
    def forecast(self, value: dict):
        self.__forecast = value
        self._property_changed('forecast')        

    @property
    def tcmCostHorizon16Day(self) -> dict:
        return self.__tcmCostHorizon16Day

    @tcmCostHorizon16Day.setter
    def tcmCostHorizon16Day(self, value: dict):
        self.__tcmCostHorizon16Day = value
        self._property_changed('tcmCostHorizon16Day')        

    @property
    def pnl(self) -> dict:
        return self.__pnl

    @pnl.setter
    def pnl(self, value: dict):
        self.__pnl = value
        self._property_changed('pnl')        

    @property
    def assetClassificationsGicsIndustryGroup(self) -> dict:
        return self.__assetClassificationsGicsIndustryGroup

    @assetClassificationsGicsIndustryGroup.setter
    def assetClassificationsGicsIndustryGroup(self, value: dict):
        self.__assetClassificationsGicsIndustryGroup = value
        self._property_changed('assetClassificationsGicsIndustryGroup')        

    @property
    def unadjustedClose(self) -> dict:
        return self.__unadjustedClose

    @unadjustedClose.setter
    def unadjustedClose(self, value: dict):
        self.__unadjustedClose = value
        self._property_changed('unadjustedClose')        

    @property
    def tcmCostHorizon4Day(self) -> dict:
        return self.__tcmCostHorizon4Day

    @tcmCostHorizon4Day.setter
    def tcmCostHorizon4Day(self, value: dict):
        self.__tcmCostHorizon4Day = value
        self._property_changed('tcmCostHorizon4Day')        

    @property
    def assetClassificationsIsPrimary(self) -> dict:
        return self.__assetClassificationsIsPrimary

    @assetClassificationsIsPrimary.setter
    def assetClassificationsIsPrimary(self, value: dict):
        self.__assetClassificationsIsPrimary = value
        self._property_changed('assetClassificationsIsPrimary')        

    @property
    def styles(self) -> dict:
        return self.__styles

    @styles.setter
    def styles(self, value: dict):
        self.__styles = value
        self._property_changed('styles')        

    @property
    def lendingSecId(self) -> dict:
        return self.__lendingSecId

    @lendingSecId.setter
    def lendingSecId(self, value: dict):
        self.__lendingSecId = value
        self._property_changed('lendingSecId')        

    @property
    def shortName(self) -> dict:
        return self.__shortName

    @shortName.setter
    def shortName(self, value: dict):
        self.__shortName = value
        self._property_changed('shortName')        

    @property
    def equityTheta(self) -> dict:
        return self.__equityTheta

    @equityTheta.setter
    def equityTheta(self, value: dict):
        self.__equityTheta = value
        self._property_changed('equityTheta')        

    @property
    def averageFillPrice(self) -> dict:
        return self.__averageFillPrice

    @averageFillPrice.setter
    def averageFillPrice(self, value: dict):
        self.__averageFillPrice = value
        self._property_changed('averageFillPrice')        

    @property
    def snowfall(self) -> dict:
        return self.__snowfall

    @snowfall.setter
    def snowfall(self, value: dict):
        self.__snowfall = value
        self._property_changed('snowfall')        

    @property
    def mic(self) -> dict:
        return self.__mic

    @mic.setter
    def mic(self, value: dict):
        self.__mic = value
        self._property_changed('mic')        

    @property
    def bidGspread(self) -> dict:
        return self.__bidGspread

    @bidGspread.setter
    def bidGspread(self, value: dict):
        self.__bidGspread = value
        self._property_changed('bidGspread')        

    @property
    def openPrice(self) -> dict:
        return self.__openPrice

    @openPrice.setter
    def openPrice(self, value: dict):
        self.__openPrice = value
        self._property_changed('openPrice')        

    @property
    def mid(self) -> dict:
        return self.__mid

    @mid.setter
    def mid(self, value: dict):
        self.__mid = value
        self._property_changed('mid')        

    @property
    def autoExecState(self) -> dict:
        return self.__autoExecState

    @autoExecState.setter
    def autoExecState(self, value: dict):
        self.__autoExecState = value
        self._property_changed('autoExecState')        

    @property
    def depthSpreadScore(self) -> dict:
        return self.__depthSpreadScore

    @depthSpreadScore.setter
    def depthSpreadScore(self, value: dict):
        self.__depthSpreadScore = value
        self._property_changed('depthSpreadScore')        

    @property
    def relativeReturnYtd(self) -> dict:
        return self.__relativeReturnYtd

    @relativeReturnYtd.setter
    def relativeReturnYtd(self, value: dict):
        self.__relativeReturnYtd = value
        self._property_changed('relativeReturnYtd')        

    @property
    def long(self) -> dict:
        return self.__long

    @long.setter
    def long(self, value: dict):
        self.__long = value
        self._property_changed('long')        

    @property
    def subAccount(self) -> dict:
        return self.__subAccount

    @subAccount.setter
    def subAccount(self, value: dict):
        self.__subAccount = value
        self._property_changed('subAccount')        

    @property
    def fairVolatility(self) -> dict:
        return self.__fairVolatility

    @fairVolatility.setter
    def fairVolatility(self, value: dict):
        self.__fairVolatility = value
        self._property_changed('fairVolatility')        

    @property
    def dollarCross(self) -> dict:
        return self.__dollarCross

    @dollarCross.setter
    def dollarCross(self, value: dict):
        self.__dollarCross = value
        self._property_changed('dollarCross')        

    @property
    def portfolioType(self) -> dict:
        return self.__portfolioType

    @portfolioType.setter
    def portfolioType(self, value: dict):
        self.__portfolioType = value
        self._property_changed('portfolioType')        

    @property
    def longWeight(self) -> dict:
        return self.__longWeight

    @longWeight.setter
    def longWeight(self, value: dict):
        self.__longWeight = value
        self._property_changed('longWeight')        

    @property
    def calculationTime(self) -> dict:
        return self.__calculationTime

    @calculationTime.setter
    def calculationTime(self, value: dict):
        self.__calculationTime = value
        self._property_changed('calculationTime')        

    @property
    def vendor(self) -> dict:
        return self.__vendor

    @vendor.setter
    def vendor(self, value: dict):
        self.__vendor = value
        self._property_changed('vendor')        

    @property
    def currency(self) -> dict:
        return self.__currency

    @currency.setter
    def currency(self, value: dict):
        self.__currency = value
        self._property_changed('currency')        

    @property
    def realTimeRestrictionStatus(self) -> dict:
        return self.__realTimeRestrictionStatus

    @realTimeRestrictionStatus.setter
    def realTimeRestrictionStatus(self, value: dict):
        self.__realTimeRestrictionStatus = value
        self._property_changed('realTimeRestrictionStatus')        

    @property
    def averageRealizedVariance(self) -> dict:
        return self.__averageRealizedVariance

    @averageRealizedVariance.setter
    def averageRealizedVariance(self, value: dict):
        self.__averageRealizedVariance = value
        self._property_changed('averageRealizedVariance')        

    @property
    def clusterClass(self) -> dict:
        return self.__clusterClass

    @clusterClass.setter
    def clusterClass(self, value: dict):
        self.__clusterClass = value
        self._property_changed('clusterClass')        

    @property
    def financialReturnsScore(self) -> dict:
        return self.__financialReturnsScore

    @financialReturnsScore.setter
    def financialReturnsScore(self, value: dict):
        self.__financialReturnsScore = value
        self._property_changed('financialReturnsScore')        

    @property
    def netChange(self) -> dict:
        return self.__netChange

    @netChange.setter
    def netChange(self, value: dict):
        self.__netChange = value
        self._property_changed('netChange')        

    @property
    def nonSymbolDimensions(self) -> dict:
        return self.__nonSymbolDimensions

    @nonSymbolDimensions.setter
    def nonSymbolDimensions(self, value: dict):
        self.__nonSymbolDimensions = value
        self._property_changed('nonSymbolDimensions')        

    @property
    def queueingTime(self) -> dict:
        return self.__queueingTime

    @queueingTime.setter
    def queueingTime(self, value: dict):
        self.__queueingTime = value
        self._property_changed('queueingTime')        

    @property
    def bidSize(self) -> dict:
        return self.__bidSize

    @bidSize.setter
    def bidSize(self, value: dict):
        self.__bidSize = value
        self._property_changed('bidSize')        

    @property
    def swapType(self) -> dict:
        return self.__swapType

    @swapType.setter
    def swapType(self, value: dict):
        self.__swapType = value
        self._property_changed('swapType')        

    @property
    def arrivalMid(self) -> dict:
        return self.__arrivalMid

    @arrivalMid.setter
    def arrivalMid(self, value: dict):
        self.__arrivalMid = value
        self._property_changed('arrivalMid')        

    @property
    def assetParametersExchangeCurrency(self) -> dict:
        return self.__assetParametersExchangeCurrency

    @assetParametersExchangeCurrency.setter
    def assetParametersExchangeCurrency(self, value: dict):
        self.__assetParametersExchangeCurrency = value
        self._property_changed('assetParametersExchangeCurrency')        

    @property
    def unexplained(self) -> dict:
        return self.__unexplained

    @unexplained.setter
    def unexplained(self, value: dict):
        self.__unexplained = value
        self._property_changed('unexplained')        

    @property
    def assetClassificationsCountryName(self) -> dict:
        return self.__assetClassificationsCountryName

    @assetClassificationsCountryName.setter
    def assetClassificationsCountryName(self, value: dict):
        self.__assetClassificationsCountryName = value
        self._property_changed('assetClassificationsCountryName')        

    @property
    def metric(self) -> dict:
        return self.__metric

    @metric.setter
    def metric(self, value: dict):
        self.__metric = value
        self._property_changed('metric')        

    @property
    def newIdeasYtd(self) -> dict:
        return self.__newIdeasYtd

    @newIdeasYtd.setter
    def newIdeasYtd(self, value: dict):
        self.__newIdeasYtd = value
        self._property_changed('newIdeasYtd')        

    @property
    def managementFee(self) -> dict:
        return self.__managementFee

    @managementFee.setter
    def managementFee(self, value: dict):
        self.__managementFee = value
        self._property_changed('managementFee')        

    @property
    def ask(self) -> dict:
        return self.__ask

    @ask.setter
    def ask(self, value: dict):
        self.__ask = value
        self._property_changed('ask')        

    @property
    def impliedLognormalVolatility(self) -> dict:
        return self.__impliedLognormalVolatility

    @impliedLognormalVolatility.setter
    def impliedLognormalVolatility(self, value: dict):
        self.__impliedLognormalVolatility = value
        self._property_changed('impliedLognormalVolatility')        

    @property
    def closePrice(self) -> dict:
        return self.__closePrice

    @closePrice.setter
    def closePrice(self, value: dict):
        self.__closePrice = value
        self._property_changed('closePrice')        

    @property
    def open(self) -> dict:
        return self.__open

    @open.setter
    def open(self, value: dict):
        self.__open = value
        self._property_changed('open')        

    @property
    def sourceId(self) -> dict:
        return self.__sourceId

    @sourceId.setter
    def sourceId(self, value: dict):
        self.__sourceId = value
        self._property_changed('sourceId')        

    @property
    def country(self) -> dict:
        return self.__country

    @country.setter
    def country(self, value: dict):
        self.__country = value
        self._property_changed('country')        

    @property
    def cusip(self) -> dict:
        return self.__cusip

    @cusip.setter
    def cusip(self, value: dict):
        self.__cusip = value
        self._property_changed('cusip')        

    @property
    def touchSpreadScore(self) -> dict:
        return self.__touchSpreadScore

    @touchSpreadScore.setter
    def touchSpreadScore(self, value: dict):
        self.__touchSpreadScore = value
        self._property_changed('touchSpreadScore')        

    @property
    def absoluteStrike(self) -> dict:
        return self.__absoluteStrike

    @absoluteStrike.setter
    def absoluteStrike(self, value: dict):
        self.__absoluteStrike = value
        self._property_changed('absoluteStrike')        

    @property
    def netExposure(self) -> dict:
        return self.__netExposure

    @netExposure.setter
    def netExposure(self, value: dict):
        self.__netExposure = value
        self._property_changed('netExposure')        

    @property
    def source(self) -> dict:
        return self.__source

    @source.setter
    def source(self, value: dict):
        self.__source = value
        self._property_changed('source')        

    @property
    def assetClassificationsCountryCode(self) -> dict:
        return self.__assetClassificationsCountryCode

    @assetClassificationsCountryCode.setter
    def assetClassificationsCountryCode(self, value: dict):
        self.__assetClassificationsCountryCode = value
        self._property_changed('assetClassificationsCountryCode')        

    @property
    def frequency(self) -> dict:
        return self.__frequency

    @frequency.setter
    def frequency(self, value: dict):
        self.__frequency = value
        self._property_changed('frequency')        

    @property
    def activityId(self) -> dict:
        return self.__activityId

    @activityId.setter
    def activityId(self, value: dict):
        self.__activityId = value
        self._property_changed('activityId')        

    @property
    def estimatedImpact(self) -> dict:
        return self.__estimatedImpact

    @estimatedImpact.setter
    def estimatedImpact(self, value: dict):
        self.__estimatedImpact = value
        self._property_changed('estimatedImpact')        

    @property
    def dataSetSubCategory(self) -> dict:
        return self.__dataSetSubCategory

    @dataSetSubCategory.setter
    def dataSetSubCategory(self, value: dict):
        self.__dataSetSubCategory = value
        self._property_changed('dataSetSubCategory')        

    @property
    def loanSpreadBucket(self) -> dict:
        return self.__loanSpreadBucket

    @loanSpreadBucket.setter
    def loanSpreadBucket(self, value: dict):
        self.__loanSpreadBucket = value
        self._property_changed('loanSpreadBucket')        

    @property
    def assetParametersPricingLocation(self) -> dict:
        return self.__assetParametersPricingLocation

    @assetParametersPricingLocation.setter
    def assetParametersPricingLocation(self, value: dict):
        self.__assetParametersPricingLocation = value
        self._property_changed('assetParametersPricingLocation')        

    @property
    def eventDescription(self) -> dict:
        return self.__eventDescription

    @eventDescription.setter
    def eventDescription(self, value: dict):
        self.__eventDescription = value
        self._property_changed('eventDescription')        

    @property
    def strikeReference(self) -> dict:
        return self.__strikeReference

    @strikeReference.setter
    def strikeReference(self, value: dict):
        self.__strikeReference = value
        self._property_changed('strikeReference')        

    @property
    def details(self) -> dict:
        return self.__details

    @details.setter
    def details(self, value: dict):
        self.__details = value
        self._property_changed('details')        

    @property
    def assetCount(self) -> dict:
        return self.__assetCount

    @assetCount.setter
    def assetCount(self, value: dict):
        self.__assetCount = value
        self._property_changed('assetCount')        

    @property
    def quantityBucket(self) -> dict:
        return self.__quantityBucket

    @quantityBucket.setter
    def quantityBucket(self, value: dict):
        self.__quantityBucket = value
        self._property_changed('quantityBucket')        

    @property
    def oeName(self) -> dict:
        return self.__oeName

    @oeName.setter
    def oeName(self, value: dict):
        self.__oeName = value
        self._property_changed('oeName')        

    @property
    def given(self) -> dict:
        return self.__given

    @given.setter
    def given(self, value: dict):
        self.__given = value
        self._property_changed('given')        

    @property
    def absoluteValue(self) -> dict:
        return self.__absoluteValue

    @absoluteValue.setter
    def absoluteValue(self, value: dict):
        self.__absoluteValue = value
        self._property_changed('absoluteValue')        

    @property
    def delistingDate(self) -> dict:
        return self.__delistingDate

    @delistingDate.setter
    def delistingDate(self, value: dict):
        self.__delistingDate = value
        self._property_changed('delistingDate')        

    @property
    def longTenor(self) -> dict:
        return self.__longTenor

    @longTenor.setter
    def longTenor(self, value: dict):
        self.__longTenor = value
        self._property_changed('longTenor')        

    @property
    def mctr(self) -> dict:
        return self.__mctr

    @mctr.setter
    def mctr(self, value: dict):
        self.__mctr = value
        self._property_changed('mctr')        

    @property
    def weight(self) -> dict:
        return self.__weight

    @weight.setter
    def weight(self, value: dict):
        self.__weight = value
        self._property_changed('weight')        

    @property
    def historicalClose(self) -> dict:
        return self.__historicalClose

    @historicalClose.setter
    def historicalClose(self, value: dict):
        self.__historicalClose = value
        self._property_changed('historicalClose')        

    @property
    def assetCountPriced(self) -> dict:
        return self.__assetCountPriced

    @assetCountPriced.setter
    def assetCountPriced(self, value: dict):
        self.__assetCountPriced = value
        self._property_changed('assetCountPriced')        

    @property
    def marketDataPoint(self) -> dict:
        return self.__marketDataPoint

    @marketDataPoint.setter
    def marketDataPoint(self, value: dict):
        self.__marketDataPoint = value
        self._property_changed('marketDataPoint')        

    @property
    def ideaId(self) -> dict:
        return self.__ideaId

    @ideaId.setter
    def ideaId(self, value: dict):
        self.__ideaId = value
        self._property_changed('ideaId')        

    @property
    def commentStatus(self) -> dict:
        return self.__commentStatus

    @commentStatus.setter
    def commentStatus(self, value: dict):
        self.__commentStatus = value
        self._property_changed('commentStatus')        

    @property
    def marginalCost(self) -> dict:
        return self.__marginalCost

    @marginalCost.setter
    def marginalCost(self, value: dict):
        self.__marginalCost = value
        self._property_changed('marginalCost')        

    @property
    def absoluteWeight(self) -> dict:
        return self.__absoluteWeight

    @absoluteWeight.setter
    def absoluteWeight(self, value: dict):
        self.__absoluteWeight = value
        self._property_changed('absoluteWeight')        

    @property
    def measure(self) -> dict:
        return self.__measure

    @measure.setter
    def measure(self, value: dict):
        self.__measure = value
        self._property_changed('measure')        

    @property
    def clientWeight(self) -> dict:
        return self.__clientWeight

    @clientWeight.setter
    def clientWeight(self, value: dict):
        self.__clientWeight = value
        self._property_changed('clientWeight')        

    @property
    def hedgeAnnualizedVolatility(self) -> dict:
        return self.__hedgeAnnualizedVolatility

    @hedgeAnnualizedVolatility.setter
    def hedgeAnnualizedVolatility(self, value: dict):
        self.__hedgeAnnualizedVolatility = value
        self._property_changed('hedgeAnnualizedVolatility')        

    @property
    def benchmarkCurrency(self) -> dict:
        return self.__benchmarkCurrency

    @benchmarkCurrency.setter
    def benchmarkCurrency(self, value: dict):
        self.__benchmarkCurrency = value
        self._property_changed('benchmarkCurrency')        

    @property
    def name(self) -> dict:
        return self.__name

    @name.setter
    def name(self, value: dict):
        self.__name = value
        self._property_changed('name')        

    @property
    def aum(self) -> dict:
        return self.__aum

    @aum.setter
    def aum(self, value: dict):
        self.__aum = value
        self._property_changed('aum')        

    @property
    def folderName(self) -> dict:
        return self.__folderName

    @folderName.setter
    def folderName(self, value: dict):
        self.__folderName = value
        self._property_changed('folderName')        

    @property
    def lendingPartnerFee(self) -> dict:
        return self.__lendingPartnerFee

    @lendingPartnerFee.setter
    def lendingPartnerFee(self, value: dict):
        self.__lendingPartnerFee = value
        self._property_changed('lendingPartnerFee')        

    @property
    def region(self) -> dict:
        return self.__region

    @region.setter
    def region(self, value: dict):
        self.__region = value
        self._property_changed('region')        

    @property
    def liveDate(self) -> dict:
        return self.__liveDate

    @liveDate.setter
    def liveDate(self, value: dict):
        self.__liveDate = value
        self._property_changed('liveDate')        

    @property
    def askHigh(self) -> dict:
        return self.__askHigh

    @askHigh.setter
    def askHigh(self, value: dict):
        self.__askHigh = value
        self._property_changed('askHigh')        

    @property
    def corporateActionType(self) -> dict:
        return self.__corporateActionType

    @corporateActionType.setter
    def corporateActionType(self, value: dict):
        self.__corporateActionType = value
        self._property_changed('corporateActionType')        

    @property
    def primeId(self) -> dict:
        return self.__primeId

    @primeId.setter
    def primeId(self, value: dict):
        self.__primeId = value
        self._property_changed('primeId')        

    @property
    def tenor2(self) -> dict:
        return self.__tenor2

    @tenor2.setter
    def tenor2(self, value: dict):
        self.__tenor2 = value
        self._property_changed('tenor2')        

    @property
    def description(self) -> dict:
        return self.__description

    @description.setter
    def description(self, value: dict):
        self.__description = value
        self._property_changed('description')        

    @property
    def valueRevised(self) -> dict:
        return self.__valueRevised

    @valueRevised.setter
    def valueRevised(self, value: dict):
        self.__valueRevised = value
        self._property_changed('valueRevised')        

    @property
    def ownerName(self) -> dict:
        return self.__ownerName

    @ownerName.setter
    def ownerName(self, value: dict):
        self.__ownerName = value
        self._property_changed('ownerName')        

    @property
    def adjustedTradePrice(self) -> dict:
        return self.__adjustedTradePrice

    @adjustedTradePrice.setter
    def adjustedTradePrice(self, value: dict):
        self.__adjustedTradePrice = value
        self._property_changed('adjustedTradePrice')        

    @property
    def lastUpdatedById(self) -> dict:
        return self.__lastUpdatedById

    @lastUpdatedById.setter
    def lastUpdatedById(self, value: dict):
        self.__lastUpdatedById = value
        self._property_changed('lastUpdatedById')        

    @property
    def zScore(self) -> dict:
        return self.__zScore

    @zScore.setter
    def zScore(self, value: dict):
        self.__zScore = value
        self._property_changed('zScore')        

    @property
    def targetShareholderMeetingDate(self) -> dict:
        return self.__targetShareholderMeetingDate

    @targetShareholderMeetingDate.setter
    def targetShareholderMeetingDate(self, value: dict):
        self.__targetShareholderMeetingDate = value
        self._property_changed('targetShareholderMeetingDate')        

    @property
    def collateralMarketValue(self) -> dict:
        return self.__collateralMarketValue

    @collateralMarketValue.setter
    def collateralMarketValue(self, value: dict):
        self.__collateralMarketValue = value
        self._property_changed('collateralMarketValue')        

    @property
    def isADR(self) -> dict:
        return self.__isADR

    @isADR.setter
    def isADR(self, value: dict):
        self.__isADR = value
        self._property_changed('isADR')        

    @property
    def eventStartTime(self) -> dict:
        return self.__eventStartTime

    @eventStartTime.setter
    def eventStartTime(self, value: dict):
        self.__eventStartTime = value
        self._property_changed('eventStartTime')        

    @property
    def factor(self) -> dict:
        return self.__factor

    @factor.setter
    def factor(self, value: dict):
        self.__factor = value
        self._property_changed('factor')        

    @property
    def daysOnLoan(self) -> dict:
        return self.__daysOnLoan

    @daysOnLoan.setter
    def daysOnLoan(self, value: dict):
        self.__daysOnLoan = value
        self._property_changed('daysOnLoan')        

    @property
    def longConvictionSmall(self) -> dict:
        return self.__longConvictionSmall

    @longConvictionSmall.setter
    def longConvictionSmall(self, value: dict):
        self.__longConvictionSmall = value
        self._property_changed('longConvictionSmall')        

    @property
    def serviceId(self) -> dict:
        return self.__serviceId

    @serviceId.setter
    def serviceId(self, value: dict):
        self.__serviceId = value
        self._property_changed('serviceId')        

    @property
    def turnover(self) -> dict:
        return self.__turnover

    @turnover.setter
    def turnover(self, value: dict):
        self.__turnover = value
        self._property_changed('turnover')        

    @property
    def gsfeer(self) -> dict:
        return self.__gsfeer

    @gsfeer.setter
    def gsfeer(self, value: dict):
        self.__gsfeer = value
        self._property_changed('gsfeer')        

    @property
    def coverage(self) -> dict:
        return self.__coverage

    @coverage.setter
    def coverage(self, value: dict):
        self.__coverage = value
        self._property_changed('coverage')        

    @property
    def backtestId(self) -> dict:
        return self.__backtestId

    @backtestId.setter
    def backtestId(self, value: dict):
        self.__backtestId = value
        self._property_changed('backtestId')        

    @property
    def gPercentile(self) -> dict:
        return self.__gPercentile

    @gPercentile.setter
    def gPercentile(self, value: dict):
        self.__gPercentile = value
        self._property_changed('gPercentile')        

    @property
    def gScore(self) -> dict:
        return self.__gScore

    @gScore.setter
    def gScore(self, value: dict):
        self.__gScore = value
        self._property_changed('gScore')        

    @property
    def marketValue(self) -> dict:
        return self.__marketValue

    @marketValue.setter
    def marketValue(self, value: dict):
        self.__marketValue = value
        self._property_changed('marketValue')        

    @property
    def multipleScore(self) -> dict:
        return self.__multipleScore

    @multipleScore.setter
    def multipleScore(self, value: dict):
        self.__multipleScore = value
        self._property_changed('multipleScore')        

    @property
    def lendingFundNav(self) -> dict:
        return self.__lendingFundNav

    @lendingFundNav.setter
    def lendingFundNav(self, value: dict):
        self.__lendingFundNav = value
        self._property_changed('lendingFundNav')        

    @property
    def sourceOriginalCategory(self) -> dict:
        return self.__sourceOriginalCategory

    @sourceOriginalCategory.setter
    def sourceOriginalCategory(self, value: dict):
        self.__sourceOriginalCategory = value
        self._property_changed('sourceOriginalCategory')        

    @property
    def betaAdjustedExposure(self) -> dict:
        return self.__betaAdjustedExposure

    @betaAdjustedExposure.setter
    def betaAdjustedExposure(self, value: dict):
        self.__betaAdjustedExposure = value
        self._property_changed('betaAdjustedExposure')        

    @property
    def composite5DayAdv(self) -> dict:
        return self.__composite5DayAdv

    @composite5DayAdv.setter
    def composite5DayAdv(self, value: dict):
        self.__composite5DayAdv = value
        self._property_changed('composite5DayAdv')        

    @property
    def dividendPoints(self) -> dict:
        return self.__dividendPoints

    @dividendPoints.setter
    def dividendPoints(self, value: dict):
        self.__dividendPoints = value
        self._property_changed('dividendPoints')        

    @property
    def newIdeasWtd(self) -> dict:
        return self.__newIdeasWtd

    @newIdeasWtd.setter
    def newIdeasWtd(self, value: dict):
        self.__newIdeasWtd = value
        self._property_changed('newIdeasWtd')        

    @property
    def paid(self) -> dict:
        return self.__paid

    @paid.setter
    def paid(self, value: dict):
        self.__paid = value
        self._property_changed('paid')        

    @property
    def short(self) -> dict:
        return self.__short

    @short.setter
    def short(self, value: dict):
        self.__short = value
        self._property_changed('short')        

    @property
    def location(self) -> dict:
        return self.__location

    @location.setter
    def location(self, value: dict):
        self.__location = value
        self._property_changed('location')        

    @property
    def comment(self) -> dict:
        return self.__comment

    @comment.setter
    def comment(self, value: dict):
        self.__comment = value
        self._property_changed('comment')        

    @property
    def bosInTicksDescription(self) -> dict:
        return self.__bosInTicksDescription

    @bosInTicksDescription.setter
    def bosInTicksDescription(self, value: dict):
        self.__bosInTicksDescription = value
        self._property_changed('bosInTicksDescription')        

    @property
    def sourceSymbol(self) -> dict:
        return self.__sourceSymbol

    @sourceSymbol.setter
    def sourceSymbol(self, value: dict):
        self.__sourceSymbol = value
        self._property_changed('sourceSymbol')        

    @property
    def scenarioId(self) -> dict:
        return self.__scenarioId

    @scenarioId.setter
    def scenarioId(self, value: dict):
        self.__scenarioId = value
        self._property_changed('scenarioId')        

    @property
    def askUnadjusted(self) -> dict:
        return self.__askUnadjusted

    @askUnadjusted.setter
    def askUnadjusted(self, value: dict):
        self.__askUnadjusted = value
        self._property_changed('askUnadjusted')        

    @property
    def queueClockTime(self) -> dict:
        return self.__queueClockTime

    @queueClockTime.setter
    def queueClockTime(self, value: dict):
        self.__queueClockTime = value
        self._property_changed('queueClockTime')        

    @property
    def askChange(self) -> dict:
        return self.__askChange

    @askChange.setter
    def askChange(self, value: dict):
        self.__askChange = value
        self._property_changed('askChange')        

    @property
    def impliedCorrelation(self) -> dict:
        return self.__impliedCorrelation

    @impliedCorrelation.setter
    def impliedCorrelation(self, value: dict):
        self.__impliedCorrelation = value
        self._property_changed('impliedCorrelation')        

    @property
    def tcmCostParticipationRate50Pct(self) -> dict:
        return self.__tcmCostParticipationRate50Pct

    @tcmCostParticipationRate50Pct.setter
    def tcmCostParticipationRate50Pct(self, value: dict):
        self.__tcmCostParticipationRate50Pct = value
        self._property_changed('tcmCostParticipationRate50Pct')        

    @property
    def normalizedPerformance(self) -> dict:
        return self.__normalizedPerformance

    @normalizedPerformance.setter
    def normalizedPerformance(self, value: dict):
        self.__normalizedPerformance = value
        self._property_changed('normalizedPerformance')        

    @property
    def cmId(self) -> dict:
        return self.__cmId

    @cmId.setter
    def cmId(self, value: dict):
        self.__cmId = value
        self._property_changed('cmId')        

    @property
    def type(self) -> dict:
        return self.__type

    @type.setter
    def type(self, value: dict):
        self.__type = value
        self._property_changed('type')        

    @property
    def mdapi(self) -> dict:
        return self.__mdapi

    @mdapi.setter
    def mdapi(self, value: dict):
        self.__mdapi = value
        self._property_changed('mdapi')        

    @property
    def dividendYield(self) -> dict:
        return self.__dividendYield

    @dividendYield.setter
    def dividendYield(self, value: dict):
        self.__dividendYield = value
        self._property_changed('dividendYield')        

    @property
    def cumulativePnl(self) -> dict:
        return self.__cumulativePnl

    @cumulativePnl.setter
    def cumulativePnl(self, value: dict):
        self.__cumulativePnl = value
        self._property_changed('cumulativePnl')        

    @property
    def sourceOrigin(self) -> dict:
        return self.__sourceOrigin

    @sourceOrigin.setter
    def sourceOrigin(self, value: dict):
        self.__sourceOrigin = value
        self._property_changed('sourceOrigin')        

    @property
    def shortTenor(self) -> dict:
        return self.__shortTenor

    @shortTenor.setter
    def shortTenor(self, value: dict):
        self.__shortTenor = value
        self._property_changed('shortTenor')        

    @property
    def loss(self) -> dict:
        return self.__loss

    @loss.setter
    def loss(self, value: dict):
        self.__loss = value
        self._property_changed('loss')        

    @property
    def unadjustedVolume(self) -> dict:
        return self.__unadjustedVolume

    @unadjustedVolume.setter
    def unadjustedVolume(self, value: dict):
        self.__unadjustedVolume = value
        self._property_changed('unadjustedVolume')        

    @property
    def measures(self) -> dict:
        return self.__measures

    @measures.setter
    def measures(self, value: dict):
        self.__measures = value
        self._property_changed('measures')        

    @property
    def tradingCostPnl(self) -> dict:
        return self.__tradingCostPnl

    @tradingCostPnl.setter
    def tradingCostPnl(self, value: dict):
        self.__tradingCostPnl = value
        self._property_changed('tradingCostPnl')        

    @property
    def internalUser(self) -> dict:
        return self.__internalUser

    @internalUser.setter
    def internalUser(self, value: dict):
        self.__internalUser = value
        self._property_changed('internalUser')        

    @property
    def price(self) -> dict:
        return self.__price

    @price.setter
    def price(self, value: dict):
        self.__price = value
        self._property_changed('price')        

    @property
    def paymentQuantity(self) -> dict:
        return self.__paymentQuantity

    @paymentQuantity.setter
    def paymentQuantity(self, value: dict):
        self.__paymentQuantity = value
        self._property_changed('paymentQuantity')        

    @property
    def underlyer(self) -> dict:
        return self.__underlyer

    @underlyer.setter
    def underlyer(self, value: dict):
        self.__underlyer = value
        self._property_changed('underlyer')        

    @property
    def positionIdx(self) -> dict:
        return self.__positionIdx

    @positionIdx.setter
    def positionIdx(self, value: dict):
        self.__positionIdx = value
        self._property_changed('positionIdx')        

    @property
    def secName(self) -> dict:
        return self.__secName

    @secName.setter
    def secName(self, value: dict):
        self.__secName = value
        self._property_changed('secName')        

    @property
    def percentADV(self) -> dict:
        return self.__percentADV

    @percentADV.setter
    def percentADV(self, value: dict):
        self.__percentADV = value
        self._property_changed('percentADV')        

    @property
    def redemptionOption(self) -> dict:
        return self.__redemptionOption

    @redemptionOption.setter
    def redemptionOption(self, value: dict):
        self.__redemptionOption = value
        self._property_changed('redemptionOption')        

    @property
    def unadjustedLow(self) -> dict:
        return self.__unadjustedLow

    @unadjustedLow.setter
    def unadjustedLow(self, value: dict):
        self.__unadjustedLow = value
        self._property_changed('unadjustedLow')        

    @property
    def contract(self) -> dict:
        return self.__contract

    @contract.setter
    def contract(self, value: dict):
        self.__contract = value
        self._property_changed('contract')        

    @property
    def sedol(self) -> dict:
        return self.__sedol

    @sedol.setter
    def sedol(self, value: dict):
        self.__sedol = value
        self._property_changed('sedol')        

    @property
    def roundingCostPnl(self) -> dict:
        return self.__roundingCostPnl

    @roundingCostPnl.setter
    def roundingCostPnl(self, value: dict):
        self.__roundingCostPnl = value
        self._property_changed('roundingCostPnl')        

    @property
    def sustainGlobal(self) -> dict:
        return self.__sustainGlobal

    @sustainGlobal.setter
    def sustainGlobal(self, value: dict):
        self.__sustainGlobal = value
        self._property_changed('sustainGlobal')        

    @property
    def sourceTicker(self) -> dict:
        return self.__sourceTicker

    @sourceTicker.setter
    def sourceTicker(self, value: dict):
        self.__sourceTicker = value
        self._property_changed('sourceTicker')        

    @property
    def portfolioId(self) -> dict:
        return self.__portfolioId

    @portfolioId.setter
    def portfolioId(self, value: dict):
        self.__portfolioId = value
        self._property_changed('portfolioId')        

    @property
    def gsid(self) -> dict:
        return self.__gsid

    @gsid.setter
    def gsid(self, value: dict):
        self.__gsid = value
        self._property_changed('gsid')        

    @property
    def esPercentile(self) -> dict:
        return self.__esPercentile

    @esPercentile.setter
    def esPercentile(self, value: dict):
        self.__esPercentile = value
        self._property_changed('esPercentile')        

    @property
    def lendingFund(self) -> dict:
        return self.__lendingFund

    @lendingFund.setter
    def lendingFund(self, value: dict):
        self.__lendingFund = value
        self._property_changed('lendingFund')        

    @property
    def tcmCostParticipationRate15Pct(self) -> dict:
        return self.__tcmCostParticipationRate15Pct

    @tcmCostParticipationRate15Pct.setter
    def tcmCostParticipationRate15Pct(self, value: dict):
        self.__tcmCostParticipationRate15Pct = value
        self._property_changed('tcmCostParticipationRate15Pct')        

    @property
    def sensitivity(self) -> dict:
        return self.__sensitivity

    @sensitivity.setter
    def sensitivity(self, value: dict):
        self.__sensitivity = value
        self._property_changed('sensitivity')        

    @property
    def fiscalYear(self) -> dict:
        return self.__fiscalYear

    @fiscalYear.setter
    def fiscalYear(self, value: dict):
        self.__fiscalYear = value
        self._property_changed('fiscalYear')        

    @property
    def rcic(self) -> dict:
        return self.__rcic

    @rcic.setter
    def rcic(self, value: dict):
        self.__rcic = value
        self._property_changed('rcic')        

    @property
    def simonAssetTags(self) -> dict:
        return self.__simonAssetTags

    @simonAssetTags.setter
    def simonAssetTags(self, value: dict):
        self.__simonAssetTags = value
        self._property_changed('simonAssetTags')        

    @property
    def internal(self) -> dict:
        return self.__internal

    @internal.setter
    def internal(self, value: dict):
        self.__internal = value
        self._property_changed('internal')        

    @property
    def forwardPoint(self) -> dict:
        return self.__forwardPoint

    @forwardPoint.setter
    def forwardPoint(self, value: dict):
        self.__forwardPoint = value
        self._property_changed('forwardPoint')        

    @property
    def assetClassificationsGicsIndustry(self) -> dict:
        return self.__assetClassificationsGicsIndustry

    @assetClassificationsGicsIndustry.setter
    def assetClassificationsGicsIndustry(self, value: dict):
        self.__assetClassificationsGicsIndustry = value
        self._property_changed('assetClassificationsGicsIndustry')        

    @property
    def adjustedBidPrice(self) -> dict:
        return self.__adjustedBidPrice

    @adjustedBidPrice.setter
    def adjustedBidPrice(self, value: dict):
        self.__adjustedBidPrice = value
        self._property_changed('adjustedBidPrice')        

    @property
    def hitRateQtd(self) -> dict:
        return self.__hitRateQtd

    @hitRateQtd.setter
    def hitRateQtd(self, value: dict):
        self.__hitRateQtd = value
        self._property_changed('hitRateQtd')        

    @property
    def varSwap(self) -> dict:
        return self.__varSwap

    @varSwap.setter
    def varSwap(self, value: dict):
        self.__varSwap = value
        self._property_changed('varSwap')        

    @property
    def lowUnadjusted(self) -> dict:
        return self.__lowUnadjusted

    @lowUnadjusted.setter
    def lowUnadjusted(self, value: dict):
        self.__lowUnadjusted = value
        self._property_changed('lowUnadjusted')        

    @property
    def sectorsRaw(self) -> dict:
        return self.__sectorsRaw

    @sectorsRaw.setter
    def sectorsRaw(self, value: dict):
        self.__sectorsRaw = value
        self._property_changed('sectorsRaw')        

    @property
    def recallQuantity(self) -> dict:
        return self.__recallQuantity

    @recallQuantity.setter
    def recallQuantity(self, value: dict):
        self.__recallQuantity = value
        self._property_changed('recallQuantity')        

    @property
    def low(self) -> dict:
        return self.__low

    @low.setter
    def low(self, value: dict):
        self.__low = value
        self._property_changed('low')        

    @property
    def crossGroup(self) -> dict:
        return self.__crossGroup

    @crossGroup.setter
    def crossGroup(self, value: dict):
        self.__crossGroup = value
        self._property_changed('crossGroup')        

    @property
    def integratedScore(self) -> dict:
        return self.__integratedScore

    @integratedScore.setter
    def integratedScore(self, value: dict):
        self.__integratedScore = value
        self._property_changed('integratedScore')        

    @property
    def fiveDayPriceChangeBps(self) -> dict:
        return self.__fiveDayPriceChangeBps

    @fiveDayPriceChangeBps.setter
    def fiveDayPriceChangeBps(self, value: dict):
        self.__fiveDayPriceChangeBps = value
        self._property_changed('fiveDayPriceChangeBps')        

    @property
    def tradeSize(self) -> dict:
        return self.__tradeSize

    @tradeSize.setter
    def tradeSize(self, value: dict):
        self.__tradeSize = value
        self._property_changed('tradeSize')        

    @property
    def holdings(self) -> dict:
        return self.__holdings

    @holdings.setter
    def holdings(self, value: dict):
        self.__holdings = value
        self._property_changed('holdings')        

    @property
    def symbolDimensions(self) -> dict:
        return self.__symbolDimensions

    @symbolDimensions.setter
    def symbolDimensions(self, value: dict):
        self.__symbolDimensions = value
        self._property_changed('symbolDimensions')        

    @property
    def priceMethod(self) -> dict:
        return self.__priceMethod

    @priceMethod.setter
    def priceMethod(self, value: dict):
        self.__priceMethod = value
        self._property_changed('priceMethod')        

    @property
    def quotingStyle(self) -> dict:
        return self.__quotingStyle

    @quotingStyle.setter
    def quotingStyle(self, value: dict):
        self.__quotingStyle = value
        self._property_changed('quotingStyle')        

    @property
    def scenarioGroupId(self) -> dict:
        return self.__scenarioGroupId

    @scenarioGroupId.setter
    def scenarioGroupId(self, value: dict):
        self.__scenarioGroupId = value
        self._property_changed('scenarioGroupId')        

    @property
    def errorMessage(self) -> dict:
        return self.__errorMessage

    @errorMessage.setter
    def errorMessage(self, value: dict):
        self.__errorMessage = value
        self._property_changed('errorMessage')        

    @property
    def averageImpliedVariance(self) -> dict:
        return self.__averageImpliedVariance

    @averageImpliedVariance.setter
    def averageImpliedVariance(self, value: dict):
        self.__averageImpliedVariance = value
        self._property_changed('averageImpliedVariance')        

    @property
    def avgTradeRateDescription(self) -> dict:
        return self.__avgTradeRateDescription

    @avgTradeRateDescription.setter
    def avgTradeRateDescription(self, value: dict):
        self.__avgTradeRateDescription = value
        self._property_changed('avgTradeRateDescription')        

    @property
    def midPrice(self) -> dict:
        return self.__midPrice

    @midPrice.setter
    def midPrice(self, value: dict):
        self.__midPrice = value
        self._property_changed('midPrice')        

    @property
    def fraction(self) -> dict:
        return self.__fraction

    @fraction.setter
    def fraction(self, value: dict):
        self.__fraction = value
        self._property_changed('fraction')        

    @property
    def stsCreditMarket(self) -> dict:
        return self.__stsCreditMarket

    @stsCreditMarket.setter
    def stsCreditMarket(self, value: dict):
        self.__stsCreditMarket = value
        self._property_changed('stsCreditMarket')        

    @property
    def assetCountShort(self) -> dict:
        return self.__assetCountShort

    @assetCountShort.setter
    def assetCountShort(self, value: dict):
        self.__assetCountShort = value
        self._property_changed('assetCountShort')        

    @property
    def stsEmDm(self) -> dict:
        return self.__stsEmDm

    @stsEmDm.setter
    def stsEmDm(self, value: dict):
        self.__stsEmDm = value
        self._property_changed('stsEmDm')        

    @property
    def requiredCollateralValue(self) -> dict:
        return self.__requiredCollateralValue

    @requiredCollateralValue.setter
    def requiredCollateralValue(self, value: dict):
        self.__requiredCollateralValue = value
        self._property_changed('requiredCollateralValue')        

    @property
    def tcmCostHorizon2Day(self) -> dict:
        return self.__tcmCostHorizon2Day

    @tcmCostHorizon2Day.setter
    def tcmCostHorizon2Day(self, value: dict):
        self.__tcmCostHorizon2Day = value
        self._property_changed('tcmCostHorizon2Day')        

    @property
    def pendingLoanCount(self) -> dict:
        return self.__pendingLoanCount

    @pendingLoanCount.setter
    def pendingLoanCount(self, value: dict):
        self.__pendingLoanCount = value
        self._property_changed('pendingLoanCount')        

    @property
    def queueInLots(self) -> dict:
        return self.__queueInLots

    @queueInLots.setter
    def queueInLots(self, value: dict):
        self.__queueInLots = value
        self._property_changed('queueInLots')        

    @property
    def priceRangeInTicksDescription(self) -> dict:
        return self.__priceRangeInTicksDescription

    @priceRangeInTicksDescription.setter
    def priceRangeInTicksDescription(self, value: dict):
        self.__priceRangeInTicksDescription = value
        self._property_changed('priceRangeInTicksDescription')        

    @property
    def tenderOfferExpirationDate(self) -> dict:
        return self.__tenderOfferExpirationDate

    @tenderOfferExpirationDate.setter
    def tenderOfferExpirationDate(self, value: dict):
        self.__tenderOfferExpirationDate = value
        self._property_changed('tenderOfferExpirationDate')        

    @property
    def highUnadjusted(self) -> dict:
        return self.__highUnadjusted

    @highUnadjusted.setter
    def highUnadjusted(self, value: dict):
        self.__highUnadjusted = value
        self._property_changed('highUnadjusted')        

    @property
    def sourceCategory(self) -> dict:
        return self.__sourceCategory

    @sourceCategory.setter
    def sourceCategory(self, value: dict):
        self.__sourceCategory = value
        self._property_changed('sourceCategory')        

    @property
    def volumeUnadjusted(self) -> dict:
        return self.__volumeUnadjusted

    @volumeUnadjusted.setter
    def volumeUnadjusted(self, value: dict):
        self.__volumeUnadjusted = value
        self._property_changed('volumeUnadjusted')        

    @property
    def avgTradeRateLabel(self) -> tuple:
        return self.__avgTradeRateLabel

    @avgTradeRateLabel.setter
    def avgTradeRateLabel(self, value: tuple):
        self.__avgTradeRateLabel = value
        self._property_changed('avgTradeRateLabel')        

    @property
    def tcmCostParticipationRate5Pct(self) -> dict:
        return self.__tcmCostParticipationRate5Pct

    @tcmCostParticipationRate5Pct.setter
    def tcmCostParticipationRate5Pct(self, value: dict):
        self.__tcmCostParticipationRate5Pct = value
        self._property_changed('tcmCostParticipationRate5Pct')        

    @property
    def isActive(self) -> dict:
        return self.__isActive

    @isActive.setter
    def isActive(self, value: dict):
        self.__isActive = value
        self._property_changed('isActive')        

    @property
    def growthScore(self) -> dict:
        return self.__growthScore

    @growthScore.setter
    def growthScore(self, value: dict):
        self.__growthScore = value
        self._property_changed('growthScore')        

    @property
    def bufferThreshold(self) -> dict:
        return self.__bufferThreshold

    @bufferThreshold.setter
    def bufferThreshold(self, value: dict):
        self.__bufferThreshold = value
        self._property_changed('bufferThreshold')        

    @property
    def encodedStats(self) -> dict:
        return self.__encodedStats

    @encodedStats.setter
    def encodedStats(self, value: dict):
        self.__encodedStats = value
        self._property_changed('encodedStats')        

    @property
    def adjustedShortInterest(self) -> dict:
        return self.__adjustedShortInterest

    @adjustedShortInterest.setter
    def adjustedShortInterest(self, value: dict):
        self.__adjustedShortInterest = value
        self._property_changed('adjustedShortInterest')        

    @property
    def askSize(self) -> dict:
        return self.__askSize

    @askSize.setter
    def askSize(self, value: dict):
        self.__askSize = value
        self._property_changed('askSize')        

    @property
    def mdapiType(self) -> dict:
        return self.__mdapiType

    @mdapiType.setter
    def mdapiType(self, value: dict):
        self.__mdapiType = value
        self._property_changed('mdapiType')        

    @property
    def group(self) -> dict:
        return self.__group

    @group.setter
    def group(self, value: dict):
        self.__group = value
        self._property_changed('group')        

    @property
    def estimatedSpread(self) -> dict:
        return self.__estimatedSpread

    @estimatedSpread.setter
    def estimatedSpread(self, value: dict):
        self.__estimatedSpread = value
        self._property_changed('estimatedSpread')        

    @property
    def resource(self) -> dict:
        return self.__resource

    @resource.setter
    def resource(self, value: dict):
        self.__resource = value
        self._property_changed('resource')        

    @property
    def averageRealizedVolatility(self) -> dict:
        return self.__averageRealizedVolatility

    @averageRealizedVolatility.setter
    def averageRealizedVolatility(self, value: dict):
        self.__averageRealizedVolatility = value
        self._property_changed('averageRealizedVolatility')        

    @property
    def tcmCost(self) -> dict:
        return self.__tcmCost

    @tcmCost.setter
    def tcmCost(self, value: dict):
        self.__tcmCost = value
        self._property_changed('tcmCost')        

    @property
    def sustainJapan(self) -> dict:
        return self.__sustainJapan

    @sustainJapan.setter
    def sustainJapan(self, value: dict):
        self.__sustainJapan = value
        self._property_changed('sustainJapan')        

    @property
    def navSpread(self) -> dict:
        return self.__navSpread

    @navSpread.setter
    def navSpread(self, value: dict):
        self.__navSpread = value
        self._property_changed('navSpread')        

    @property
    def bidPrice(self) -> dict:
        return self.__bidPrice

    @bidPrice.setter
    def bidPrice(self, value: dict):
        self.__bidPrice = value
        self._property_changed('bidPrice')        

    @property
    def dollarTotalReturn(self) -> dict:
        return self.__dollarTotalReturn

    @dollarTotalReturn.setter
    def dollarTotalReturn(self, value: dict):
        self.__dollarTotalReturn = value
        self._property_changed('dollarTotalReturn')        

    @property
    def hedgeTrackingError(self) -> dict:
        return self.__hedgeTrackingError

    @hedgeTrackingError.setter
    def hedgeTrackingError(self, value: dict):
        self.__hedgeTrackingError = value
        self._property_changed('hedgeTrackingError')        

    @property
    def marketCapCategory(self) -> dict:
        return self.__marketCapCategory

    @marketCapCategory.setter
    def marketCapCategory(self, value: dict):
        self.__marketCapCategory = value
        self._property_changed('marketCapCategory')        

    @property
    def historicalVolume(self) -> dict:
        return self.__historicalVolume

    @historicalVolume.setter
    def historicalVolume(self, value: dict):
        self.__historicalVolume = value
        self._property_changed('historicalVolume')        

    @property
    def esNumericPercentile(self) -> dict:
        return self.__esNumericPercentile

    @esNumericPercentile.setter
    def esNumericPercentile(self, value: dict):
        self.__esNumericPercentile = value
        self._property_changed('esNumericPercentile')        

    @property
    def strikePrice(self) -> dict:
        return self.__strikePrice

    @strikePrice.setter
    def strikePrice(self, value: dict):
        self.__strikePrice = value
        self._property_changed('strikePrice')        

    @property
    def askGspread(self) -> dict:
        return self.__askGspread

    @askGspread.setter
    def askGspread(self, value: dict):
        self.__askGspread = value
        self._property_changed('askGspread')        

    @property
    def calSpreadMisPricing(self) -> dict:
        return self.__calSpreadMisPricing

    @calSpreadMisPricing.setter
    def calSpreadMisPricing(self, value: dict):
        self.__calSpreadMisPricing = value
        self._property_changed('calSpreadMisPricing')        

    @property
    def equityGamma(self) -> dict:
        return self.__equityGamma

    @equityGamma.setter
    def equityGamma(self, value: dict):
        self.__equityGamma = value
        self._property_changed('equityGamma')        

    @property
    def grossIncome(self) -> dict:
        return self.__grossIncome

    @grossIncome.setter
    def grossIncome(self, value: dict):
        self.__grossIncome = value
        self._property_changed('grossIncome')        

    @property
    def emId(self) -> dict:
        return self.__emId

    @emId.setter
    def emId(self, value: dict):
        self.__emId = value
        self._property_changed('emId')        

    @property
    def adjustedOpenPrice(self) -> dict:
        return self.__adjustedOpenPrice

    @adjustedOpenPrice.setter
    def adjustedOpenPrice(self, value: dict):
        self.__adjustedOpenPrice = value
        self._property_changed('adjustedOpenPrice')        

    @property
    def assetCountInModel(self) -> dict:
        return self.__assetCountInModel

    @assetCountInModel.setter
    def assetCountInModel(self, value: dict):
        self.__assetCountInModel = value
        self._property_changed('assetCountInModel')        

    @property
    def stsCreditRegion(self) -> dict:
        return self.__stsCreditRegion

    @stsCreditRegion.setter
    def stsCreditRegion(self, value: dict):
        self.__stsCreditRegion = value
        self._property_changed('stsCreditRegion')        

    @property
    def point(self) -> dict:
        return self.__point

    @point.setter
    def point(self, value: dict):
        self.__point = value
        self._property_changed('point')        

    @property
    def totalReturns(self) -> dict:
        return self.__totalReturns

    @totalReturns.setter
    def totalReturns(self, value: dict):
        self.__totalReturns = value
        self._property_changed('totalReturns')        

    @property
    def lender(self) -> dict:
        return self.__lender

    @lender.setter
    def lender(self, value: dict):
        self.__lender = value
        self._property_changed('lender')        

    @property
    def minTemperature(self) -> dict:
        return self.__minTemperature

    @minTemperature.setter
    def minTemperature(self, value: dict):
        self.__minTemperature = value
        self._property_changed('minTemperature')        

    @property
    def value(self) -> dict:
        return self.__value

    @value.setter
    def value(self, value: dict):
        self.__value = value
        self._property_changed('value')        

    @property
    def relativeStrike(self) -> dict:
        return self.__relativeStrike

    @relativeStrike.setter
    def relativeStrike(self, value: dict):
        self.__relativeStrike = value
        self._property_changed('relativeStrike')        

    @property
    def amount(self) -> dict:
        return self.__amount

    @amount.setter
    def amount(self, value: dict):
        self.__amount = value
        self._property_changed('amount')        

    @property
    def quantity(self) -> dict:
        return self.__quantity

    @quantity.setter
    def quantity(self, value: dict):
        self.__quantity = value
        self._property_changed('quantity')        

    @property
    def lendingFundAcct(self) -> dict:
        return self.__lendingFundAcct

    @lendingFundAcct.setter
    def lendingFundAcct(self, value: dict):
        self.__lendingFundAcct = value
        self._property_changed('lendingFundAcct')        

    @property
    def reportId(self) -> dict:
        return self.__reportId

    @reportId.setter
    def reportId(self, value: dict):
        self.__reportId = value
        self._property_changed('reportId')        

    @property
    def indexWeight(self) -> dict:
        return self.__indexWeight

    @indexWeight.setter
    def indexWeight(self, value: dict):
        self.__indexWeight = value
        self._property_changed('indexWeight')        

    @property
    def rebate(self) -> dict:
        return self.__rebate

    @rebate.setter
    def rebate(self, value: dict):
        self.__rebate = value
        self._property_changed('rebate')        

    @property
    def flagship(self) -> dict:
        return self.__flagship

    @flagship.setter
    def flagship(self, value: dict):
        self.__flagship = value
        self._property_changed('flagship')        

    @property
    def trader(self) -> dict:
        return self.__trader

    @trader.setter
    def trader(self, value: dict):
        self.__trader = value
        self._property_changed('trader')        

    @property
    def factorCategory(self) -> dict:
        return self.__factorCategory

    @factorCategory.setter
    def factorCategory(self, value: dict):
        self.__factorCategory = value
        self._property_changed('factorCategory')        

    @property
    def impliedVolatility(self) -> dict:
        return self.__impliedVolatility

    @impliedVolatility.setter
    def impliedVolatility(self, value: dict):
        self.__impliedVolatility = value
        self._property_changed('impliedVolatility')        

    @property
    def spread(self) -> dict:
        return self.__spread

    @spread.setter
    def spread(self, value: dict):
        self.__spread = value
        self._property_changed('spread')        

    @property
    def stsRatesMaturity(self) -> dict:
        return self.__stsRatesMaturity

    @stsRatesMaturity.setter
    def stsRatesMaturity(self, value: dict):
        self.__stsRatesMaturity = value
        self._property_changed('stsRatesMaturity')        

    @property
    def equityDelta(self) -> dict:
        return self.__equityDelta

    @equityDelta.setter
    def equityDelta(self, value: dict):
        self.__equityDelta = value
        self._property_changed('equityDelta')        

    @property
    def grossWeight(self) -> dict:
        return self.__grossWeight

    @grossWeight.setter
    def grossWeight(self, value: dict):
        self.__grossWeight = value
        self._property_changed('grossWeight')        

    @property
    def listed(self) -> dict:
        return self.__listed

    @listed.setter
    def listed(self, value: dict):
        self.__listed = value
        self._property_changed('listed')        

    @property
    def variance(self) -> dict:
        return self.__variance

    @variance.setter
    def variance(self, value: dict):
        self.__variance = value
        self._property_changed('variance')        

    @property
    def tcmCostHorizon6Hour(self) -> dict:
        return self.__tcmCostHorizon6Hour

    @tcmCostHorizon6Hour.setter
    def tcmCostHorizon6Hour(self, value: dict):
        self.__tcmCostHorizon6Hour = value
        self._property_changed('tcmCostHorizon6Hour')        

    @property
    def g10Currency(self) -> dict:
        return self.__g10Currency

    @g10Currency.setter
    def g10Currency(self, value: dict):
        self.__g10Currency = value
        self._property_changed('g10Currency')        

    @property
    def shockStyle(self) -> dict:
        return self.__shockStyle

    @shockStyle.setter
    def shockStyle(self, value: dict):
        self.__shockStyle = value
        self._property_changed('shockStyle')        

    @property
    def relativePeriod(self) -> dict:
        return self.__relativePeriod

    @relativePeriod.setter
    def relativePeriod(self, value: dict):
        self.__relativePeriod = value
        self._property_changed('relativePeriod')        

    @property
    def isin(self) -> dict:
        return self.__isin

    @isin.setter
    def isin(self, value: dict):
        self.__isin = value
        self._property_changed('isin')        

    @property
    def methodology(self) -> dict:
        return self.__methodology

    @methodology.setter
    def methodology(self, value: dict):
        self.__methodology = value
        self._property_changed('methodology')        


class FieldValueMap(Base):
               
    def __init__(self, **kwargs):
        super().__init__()
        self.__queueClockTimeLabel = kwargs.get('queueClockTimeLabel')
        self.__marketPnl = kwargs.get('marketPnl')
        self.__year = kwargs.get('year')
        self.__sustainAsiaExJapan = kwargs.get('sustainAsiaExJapan')
        self.__investmentRate = kwargs.get('investmentRate')
        self.__assetClassificationsGicsSubIndustry = kwargs.get('assetClassificationsGicsSubIndustry')
        self.__mdapiClass = kwargs.get('mdapiClass')
        self.__bidUnadjusted = kwargs.get('bidUnadjusted')
        self.__economicTermsHash = kwargs.get('economicTermsHash')
        self.__neighbourAssetId = kwargs.get('neighbourAssetId')
        self.__simonIntlAssetTags = kwargs.get('simonIntlAssetTags')
        self.__path = kwargs.get('path')
        self.__availableInventory = kwargs.get('availableInventory')
        self.__clientContact = kwargs.get('clientContact')
        self.__est1DayCompletePct = kwargs.get('est1DayCompletePct')
        self.__rank = kwargs.get('rank')
        self.__dataSetCategory = kwargs.get('dataSetCategory')
        self.__createdById = kwargs.get('createdById')
        self.__vehicleType = kwargs.get('vehicleType')
        self.__dailyRisk = kwargs.get('dailyRisk')
        self.__bosInBpsLabel = kwargs.get('bosInBpsLabel')
        self.__energy = kwargs.get('energy')
        self.__marketDataType = kwargs.get('marketDataType')
        self.__sentimentScore = kwargs.get('sentimentScore')
        self.__bosInBps = kwargs.get('bosInBps')
        self.__pointClass = kwargs.get('pointClass')
        self.__fxSpot = kwargs.get('fxSpot')
        self.__bidLow = kwargs.get('bidLow')
        self.__valuePrevious = kwargs.get('valuePrevious')
        self.__fairVarianceVolatility = kwargs.get('fairVarianceVolatility')
        self.__avgTradeRate = kwargs.get('avgTradeRate')
        self.__shortLevel = kwargs.get('shortLevel')
        self.__hedgeVolatility = kwargs.get('hedgeVolatility')
        self.__version = kwargs.get('version')
        self.__tags = kwargs.get('tags')
        self.__underlyingAssetId = kwargs.get('underlyingAssetId')
        self.__clientExposure = kwargs.get('clientExposure')
        self.__correlation = kwargs.get('correlation')
        self.__exposure = kwargs.get('exposure')
        self.__gsSustainSubSector = kwargs.get('gsSustainSubSector')
        self.__domain = kwargs.get('domain')
        self.__marketDataAsset = kwargs.get('marketDataAsset')
        self.__forwardTenor = kwargs.get('forwardTenor')
        self.__unadjustedHigh = kwargs.get('unadjustedHigh')
        self.__sourceImportance = kwargs.get('sourceImportance')
        self.__eid = kwargs.get('eid')
        self.__jsn = kwargs.get('jsn')
        self.__relativeReturnQtd = kwargs.get('relativeReturnQtd')
        self.__displayName = kwargs.get('displayName')
        self.__minutesToTrade100Pct = kwargs.get('minutesToTrade100Pct')
        self.__marketModelId = kwargs.get('marketModelId')
        self.__quoteType = kwargs.get('quoteType')
        self.__realizedCorrelation = kwargs.get('realizedCorrelation')
        self.__tenor = kwargs.get('tenor')
        self.__esPolicyPercentile = kwargs.get('esPolicyPercentile')
        self.__atmFwdRate = kwargs.get('atmFwdRate')
        self.__tcmCostParticipationRate75Pct = kwargs.get('tcmCostParticipationRate75Pct')
        self.__close = kwargs.get('close')
        self.__tcmCostParticipationRate100Pct = kwargs.get('tcmCostParticipationRate100Pct')
        self.__disclaimer = kwargs.get('disclaimer')
        self.__measureIdx = kwargs.get('measureIdx')
        self.__a = kwargs.get('a')
        self.__b = kwargs.get('b')
        self.__loanFee = kwargs.get('loanFee')
        self.__c = kwargs.get('c')
        self.__equityVega = kwargs.get('equityVega')
        self.__lenderPayment = kwargs.get('lenderPayment')
        self.__deploymentVersion = kwargs.get('deploymentVersion')
        self.__fiveDayMove = kwargs.get('fiveDayMove')
        self.__borrower = kwargs.get('borrower')
        self.__valueFormat = kwargs.get('valueFormat')
        self.__performanceContribution = kwargs.get('performanceContribution')
        self.__targetNotional = kwargs.get('targetNotional')
        self.__fillLegId = kwargs.get('fillLegId')
        self.__delisted = kwargs.get('delisted')
        self.__rationale = kwargs.get('rationale')
        self.__regionalFocus = kwargs.get('regionalFocus')
        self.__volumePrimary = kwargs.get('volumePrimary')
        self.__series = kwargs.get('series')
        self.__simonId = kwargs.get('simonId')
        self.__newIdeasQtd = kwargs.get('newIdeasQtd')
        self.__congestion = kwargs.get('congestion')
        self.__adjustedAskPrice = kwargs.get('adjustedAskPrice')
        self.__quarter = kwargs.get('quarter')
        self.__factorUniverse = kwargs.get('factorUniverse')
        self.__eventCategory = kwargs.get('eventCategory')
        self.__impliedNormalVolatility = kwargs.get('impliedNormalVolatility')
        self.__unadjustedOpen = kwargs.get('unadjustedOpen')
        self.__arrivalRt = kwargs.get('arrivalRt')
        self.__criticality = kwargs.get('criticality')
        self.__transactionCost = kwargs.get('transactionCost')
        self.__servicingCostShortPnl = kwargs.get('servicingCostShortPnl')
        self.__bidAskSpread = kwargs.get('bidAskSpread')
        self.__optionType = kwargs.get('optionType')
        self.__tcmCostHorizon3Hour = kwargs.get('tcmCostHorizon3Hour')
        self.__clusterDescription = kwargs.get('clusterDescription')
        self.__creditLimit = kwargs.get('creditLimit')
        self.__positionAmount = kwargs.get('positionAmount')
        self.__numberOfPositions = kwargs.get('numberOfPositions')
        self.__windSpeed = kwargs.get('windSpeed')
        self.__openUnadjusted = kwargs.get('openUnadjusted')
        self.__maRank = kwargs.get('maRank')
        self.__eventStartDateTime = kwargs.get('eventStartDateTime')
        self.__askPrice = kwargs.get('askPrice')
        self.__eventId = kwargs.get('eventId')
        self.__borrowerId = kwargs.get('borrowerId')
        self.__dataProduct = kwargs.get('dataProduct')
        self.__sectors = kwargs.get('sectors')
        self.__mqSymbol = kwargs.get('mqSymbol')
        self.__annualizedTrackingError = kwargs.get('annualizedTrackingError')
        self.__volSwap = kwargs.get('volSwap')
        self.__annualizedRisk = kwargs.get('annualizedRisk')
        self.__bmPrimeId = kwargs.get('bmPrimeId')
        self.__corporateAction = kwargs.get('corporateAction')
        self.__conviction = kwargs.get('conviction')
        self.__grossExposure = kwargs.get('grossExposure')
        self.__benchmarkMaturity = kwargs.get('benchmarkMaturity')
        self.__gRegionalScore = kwargs.get('gRegionalScore')
        self.__volumeComposite = kwargs.get('volumeComposite')
        self.__volume = kwargs.get('volume')
        self.__factorId = kwargs.get('factorId')
        self.__hardToBorrow = kwargs.get('hardToBorrow')
        self.__adv = kwargs.get('adv')
        self.__stsFxCurrency = kwargs.get('stsFxCurrency')
        self.__wpk = kwargs.get('wpk')
        self.__shortConvictionMedium = kwargs.get('shortConvictionMedium')
        self.__bidChange = kwargs.get('bidChange')
        self.__exchange = kwargs.get('exchange')
        self.__expiration = kwargs.get('expiration')
        self.__tradePrice = kwargs.get('tradePrice')
        self.__esPolicyScore = kwargs.get('esPolicyScore')
        self.__loanId = kwargs.get('loanId')
        self.__primeIdNumeric = kwargs.get('primeIdNumeric')
        self.__cid = kwargs.get('cid')
        self.__onboarded = kwargs.get('onboarded')
        self.__liquidityScore = kwargs.get('liquidityScore')
        self.__importance = kwargs.get('importance')
        self.__sourceDateSpan = kwargs.get('sourceDateSpan')
        self.__assetClassificationsGicsSector = kwargs.get('assetClassificationsGicsSector')
        self.__underlyingDataSetId = kwargs.get('underlyingDataSetId')
        self.__stsAssetName = kwargs.get('stsAssetName')
        self.__closeUnadjusted = kwargs.get('closeUnadjusted')
        self.__valueUnit = kwargs.get('valueUnit')
        self.__bidHigh = kwargs.get('bidHigh')
        self.__adjustedLowPrice = kwargs.get('adjustedLowPrice')
        self.__netExposureClassification = kwargs.get('netExposureClassification')
        self.__longConvictionLarge = kwargs.get('longConvictionLarge')
        self.__fairVariance = kwargs.get('fairVariance')
        self.__hitRateWtd = kwargs.get('hitRateWtd')
        self.__oad = kwargs.get('oad')
        self.__bosInBpsDescription = kwargs.get('bosInBpsDescription')
        self.__lowPrice = kwargs.get('lowPrice')
        self.__realizedVolatility = kwargs.get('realizedVolatility')
        self.__rate = kwargs.get('rate')
        self.__adv22DayPct = kwargs.get('adv22DayPct')
        self.__alpha = kwargs.get('alpha')
        self.__client = kwargs.get('client')
        self.__cloneParentId = kwargs.get('cloneParentId')
        self.__company = kwargs.get('company')
        self.__convictionList = kwargs.get('convictionList')
        self.__priceRangeInTicksLabel = kwargs.get('priceRangeInTicksLabel')
        self.__ticker = kwargs.get('ticker')
        self.__inRiskModel = kwargs.get('inRiskModel')
        self.__tcmCostHorizon1Day = kwargs.get('tcmCostHorizon1Day')
        self.__servicingCostLongPnl = kwargs.get('servicingCostLongPnl')
        self.__stsRatesCountry = kwargs.get('stsRatesCountry')
        self.__meetingNumber = kwargs.get('meetingNumber')
        self.__exchangeId = kwargs.get('exchangeId')
        self.__horizon = kwargs.get('horizon')
        self.__midGspread = kwargs.get('midGspread')
        self.__tcmCostHorizon20Day = kwargs.get('tcmCostHorizon20Day')
        self.__longLevel = kwargs.get('longLevel')
        self.__sourceValueForecast = kwargs.get('sourceValueForecast')
        self.__shortConvictionLarge = kwargs.get('shortConvictionLarge')
        self.__realm = kwargs.get('realm')
        self.__bid = kwargs.get('bid')
        self.__dataDescription = kwargs.get('dataDescription')
        self.__counterPartyStatus = kwargs.get('counterPartyStatus')
        self.__composite22DayAdv = kwargs.get('composite22DayAdv')
        self.__dollarExcessReturn = kwargs.get('dollarExcessReturn')
        self.__gsn = kwargs.get('gsn')
        self.__isAggressive = kwargs.get('isAggressive')
        self.__tradeEndDate = kwargs.get('tradeEndDate')
        self.__orderId = kwargs.get('orderId')
        self.__gss = kwargs.get('gss')
        self.__percentOfMediandv1m = kwargs.get('percentOfMediandv1m')
        self.__lendables = kwargs.get('lendables')
        self.__assetClass = kwargs.get('assetClass')
        self.__gsideid = kwargs.get('gsideid')
        self.__bosInTicksLabel = kwargs.get('bosInTicksLabel')
        self.__ric = kwargs.get('ric')
        self.__positionSourceId = kwargs.get('positionSourceId')
        self.__division = kwargs.get('division')
        self.__marketCapUSD = kwargs.get('marketCapUSD')
        self.__gsSustainRegion = kwargs.get('gsSustainRegion')
        self.__deploymentId = kwargs.get('deploymentId')
        self.__highPrice = kwargs.get('highPrice')
        self.__loanStatus = kwargs.get('loanStatus')
        self.__shortWeight = kwargs.get('shortWeight')
        self.__absoluteShares = kwargs.get('absoluteShares')
        self.__action = kwargs.get('action')
        self.__model = kwargs.get('model')
        self.__id = kwargs.get('id')
        self.__arrivalHaircutVwapNormalized = kwargs.get('arrivalHaircutVwapNormalized')
        self.__priceComponent = kwargs.get('priceComponent')
        self.__queueClockTimeDescription = kwargs.get('queueClockTimeDescription')
        self.__loanRebate = kwargs.get('loanRebate')
        self.__period = kwargs.get('period')
        self.__indexCreateSource = kwargs.get('indexCreateSource')
        self.__fiscalQuarter = kwargs.get('fiscalQuarter')
        self.__deltaStrike = kwargs.get('deltaStrike')
        self.__marketImpact = kwargs.get('marketImpact')
        self.__eventType = kwargs.get('eventType')
        self.__assetCountLong = kwargs.get('assetCountLong')
        self.__valueActual = kwargs.get('valueActual')
        self.__bcid = kwargs.get('bcid')
        self.__collateralCurrency = kwargs.get('collateralCurrency')
        self.__restrictionStartDate = kwargs.get('restrictionStartDate')
        self.__originalCountry = kwargs.get('originalCountry')
        self.__touchLiquidityScore = kwargs.get('touchLiquidityScore')
        self.__field = kwargs.get('field')
        self.__factorCategoryId = kwargs.get('factorCategoryId')
        self.__spot = kwargs.get('spot')
        self.__expectedCompletionDate = kwargs.get('expectedCompletionDate')
        self.__loanValue = kwargs.get('loanValue')
        self.__tradingRestriction = kwargs.get('tradingRestriction')
        self.__skew = kwargs.get('skew')
        self.__status = kwargs.get('status')
        self.__sustainEmergingMarkets = kwargs.get('sustainEmergingMarkets')
        self.__eventDateTime = kwargs.get('eventDateTime')
        self.__totalReturnPrice = kwargs.get('totalReturnPrice')
        self.__city = kwargs.get('city')
        self.__totalPrice = kwargs.get('totalPrice')
        self.__eventSource = kwargs.get('eventSource')
        self.__qisPermNo = kwargs.get('qisPermNo')
        self.__hitRateYtd = kwargs.get('hitRateYtd')
        self.__valid = kwargs.get('valid')
        self.__stsCommodity = kwargs.get('stsCommodity')
        self.__stsCommoditySector = kwargs.get('stsCommoditySector')
        self.__exceptionStatus = kwargs.get('exceptionStatus')
        self.__salesCoverage = kwargs.get('salesCoverage')
        self.__shortExposure = kwargs.get('shortExposure')
        self.__esScore = kwargs.get('esScore')
        self.__tcmCostParticipationRate10Pct = kwargs.get('tcmCostParticipationRate10Pct')
        self.__eventTime = kwargs.get('eventTime')
        self.__positionSourceName = kwargs.get('positionSourceName')
        self.__priceRangeInTicks = kwargs.get('priceRangeInTicks')
        self.__deliveryDate = kwargs.get('deliveryDate')
        self.__arrivalHaircutVwap = kwargs.get('arrivalHaircutVwap')
        self.__interestRate = kwargs.get('interestRate')
        self.__executionDays = kwargs.get('executionDays')
        self.__recallDueDate = kwargs.get('recallDueDate')
        self.__pctChange = kwargs.get('pctChange')
        self.__side = kwargs.get('side')
        self.__numberOfRolls = kwargs.get('numberOfRolls')
        self.__agentLenderFee = kwargs.get('agentLenderFee')
        self.__complianceRestrictedStatus = kwargs.get('complianceRestrictedStatus')
        self.__forward = kwargs.get('forward')
        self.__borrowFee = kwargs.get('borrowFee')
        self.__strike = kwargs.get('strike')
        self.__updateTime = kwargs.get('updateTime')
        self.__loanSpread = kwargs.get('loanSpread')
        self.__tcmCostHorizon12Hour = kwargs.get('tcmCostHorizon12Hour')
        self.__dewPoint = kwargs.get('dewPoint')
        self.__researchCommission = kwargs.get('researchCommission')
        self.__bbid = kwargs.get('bbid')
        self.__assetClassificationsRiskCountryCode = kwargs.get('assetClassificationsRiskCountryCode')
        self.__eventStatus = kwargs.get('eventStatus')
        self.__sellDate = kwargs.get('sellDate')
        self.__effectiveDate = kwargs.get('effectiveDate')
        self.__return = kwargs.get('return_')
        self.__maxTemperature = kwargs.get('maxTemperature')
        self.__acquirerShareholderMeetingDate = kwargs.get('acquirerShareholderMeetingDate')
        self.__arrivalMidNormalized = kwargs.get('arrivalMidNormalized')
        self.__rating = kwargs.get('rating')
        self.__volatility = kwargs.get('volatility')
        self.__arrivalRtNormalized = kwargs.get('arrivalRtNormalized')
        self.__performanceFee = kwargs.get('performanceFee')
        self.__reportType = kwargs.get('reportType')
        self.__sourceURL = kwargs.get('sourceURL')
        self.__estimatedReturn = kwargs.get('estimatedReturn')
        self.__underlyingAssetIds = kwargs.get('underlyingAssetIds')
        self.__high = kwargs.get('high')
        self.__sourceLastUpdate = kwargs.get('sourceLastUpdate')
        self.__queueInLotsLabel = kwargs.get('queueInLotsLabel')
        self.__adv10DayPct = kwargs.get('adv10DayPct')
        self.__longConvictionMedium = kwargs.get('longConvictionMedium')
        self.__eventName = kwargs.get('eventName')
        self.__annualRisk = kwargs.get('annualRisk')
        self.__eti = kwargs.get('eti')
        self.__dailyTrackingError = kwargs.get('dailyTrackingError')
        self.__unadjustedBid = kwargs.get('unadjustedBid')
        self.__gsdeer = kwargs.get('gsdeer')
        self.__gRegionalPercentile = kwargs.get('gRegionalPercentile')
        self.__marketBuffer = kwargs.get('marketBuffer')
        self.__marketCap = kwargs.get('marketCap')
        self.__oeId = kwargs.get('oeId')
        self.__clusterRegion = kwargs.get('clusterRegion')
        self.__bbidEquivalent = kwargs.get('bbidEquivalent')
        self.__prevCloseAsk = kwargs.get('prevCloseAsk')
        self.__level = kwargs.get('level')
        self.__valoren = kwargs.get('valoren')
        self.__esMomentumScore = kwargs.get('esMomentumScore')
        self.__pressure = kwargs.get('pressure')
        self.__shortDescription = kwargs.get('shortDescription')
        self.__basis = kwargs.get('basis')
        self.__netWeight = kwargs.get('netWeight')
        self.__hedgeId = kwargs.get('hedgeId')
        self.__portfolioManagers = kwargs.get('portfolioManagers')
        self.__assetParametersCommoditySector = kwargs.get('assetParametersCommoditySector')
        self.__bosInTicks = kwargs.get('bosInTicks')
        self.__tcmCostHorizon8Day = kwargs.get('tcmCostHorizon8Day')
        self.__supraStrategy = kwargs.get('supraStrategy')
        self.__marketBufferThreshold = kwargs.get('marketBufferThreshold')
        self.__adv5DayPct = kwargs.get('adv5DayPct')
        self.__factorSource = kwargs.get('factorSource')
        self.__leverage = kwargs.get('leverage')
        self.__submitter = kwargs.get('submitter')
        self.__notional = kwargs.get('notional')
        self.__esDisclosurePercentage = kwargs.get('esDisclosurePercentage')
        self.__investmentIncome = kwargs.get('investmentIncome')
        self.__clientShortName = kwargs.get('clientShortName')
        self.__fwdPoints = kwargs.get('fwdPoints')
        self.__groupCategory = kwargs.get('groupCategory')
        self.__kpiId = kwargs.get('kpiId')
        self.__relativeReturnWtd = kwargs.get('relativeReturnWtd')
        self.__bidPlusAsk = kwargs.get('bidPlusAsk')
        self.__borrowCost = kwargs.get('borrowCost')
        self.__assetClassificationsRiskCountryName = kwargs.get('assetClassificationsRiskCountryName')
        self.__total = kwargs.get('total')
        self.__riskModel = kwargs.get('riskModel')
        self.__assetId = kwargs.get('assetId')
        self.__averageImpliedVolatility = kwargs.get('averageImpliedVolatility')
        self.__lastUpdatedTime = kwargs.get('lastUpdatedTime')
        self.__fairValue = kwargs.get('fairValue')
        self.__adjustedHighPrice = kwargs.get('adjustedHighPrice')
        self.__openTime = kwargs.get('openTime')
        self.__beta = kwargs.get('beta')
        self.__direction = kwargs.get('direction')
        self.__valueForecast = kwargs.get('valueForecast')
        self.__longExposure = kwargs.get('longExposure')
        self.__positionSourceType = kwargs.get('positionSourceType')
        self.__tcmCostParticipationRate20Pct = kwargs.get('tcmCostParticipationRate20Pct')
        self.__adjustedClosePrice = kwargs.get('adjustedClosePrice')
        self.__cross = kwargs.get('cross')
        self.__lmsId = kwargs.get('lmsId')
        self.__rebateRate = kwargs.get('rebateRate')
        self.__ideaStatus = kwargs.get('ideaStatus')
        self.__participationRate = kwargs.get('participationRate')
        self.__obfr = kwargs.get('obfr')
        self.__fxForecast = kwargs.get('fxForecast')
        self.__fixingTimeLabel = kwargs.get('fixingTimeLabel')
        self.__implementationId = kwargs.get('implementationId')
        self.__fillId = kwargs.get('fillId')
        self.__excessReturns = kwargs.get('excessReturns')
        self.__esMomentumPercentile = kwargs.get('esMomentumPercentile')
        self.__dollarReturn = kwargs.get('dollarReturn')
        self.__esNumericScore = kwargs.get('esNumericScore')
        self.__lenderIncomeAdjustment = kwargs.get('lenderIncomeAdjustment')
        self.__inBenchmark = kwargs.get('inBenchmark')
        self.__strategy = kwargs.get('strategy')
        self.__positionType = kwargs.get('positionType')
        self.__lenderIncome = kwargs.get('lenderIncome')
        self.__shortInterest = kwargs.get('shortInterest')
        self.__referencePeriod = kwargs.get('referencePeriod')
        self.__adjustedVolume = kwargs.get('adjustedVolume')
        self.__restrictionEndDate = kwargs.get('restrictionEndDate')
        self.__queueInLotsDescription = kwargs.get('queueInLotsDescription')
        self.__pbClientId = kwargs.get('pbClientId')
        self.__ownerId = kwargs.get('ownerId')
        self.__secDB = kwargs.get('secDB')
        self.__composite10DayAdv = kwargs.get('composite10DayAdv')
        self.__objective = kwargs.get('objective')
        self.__bpeQualityStars = kwargs.get('bpeQualityStars')
        self.__navPrice = kwargs.get('navPrice')
        self.__ideaActivityType = kwargs.get('ideaActivityType')
        self.__precipitation = kwargs.get('precipitation')
        self.__ideaSource = kwargs.get('ideaSource')
        self.__hedgeNotional = kwargs.get('hedgeNotional')
        self.__askLow = kwargs.get('askLow')
        self.__unadjustedAsk = kwargs.get('unadjustedAsk')
        self.__betaAdjustedNetExposure = kwargs.get('betaAdjustedNetExposure')
        self.__expiry = kwargs.get('expiry')
        self.__tradingPnl = kwargs.get('tradingPnl')
        self.__strikePercentage = kwargs.get('strikePercentage')
        self.__excessReturnPrice = kwargs.get('excessReturnPrice')
        self.__givenPlusPaid = kwargs.get('givenPlusPaid')
        self.__shortConvictionSmall = kwargs.get('shortConvictionSmall')
        self.__prevCloseBid = kwargs.get('prevCloseBid')
        self.__fxPnl = kwargs.get('fxPnl')
        self.__forecast = kwargs.get('forecast')
        self.__tcmCostHorizon16Day = kwargs.get('tcmCostHorizon16Day')
        self.__pnl = kwargs.get('pnl')
        self.__assetClassificationsGicsIndustryGroup = kwargs.get('assetClassificationsGicsIndustryGroup')
        self.__unadjustedClose = kwargs.get('unadjustedClose')
        self.__tcmCostHorizon4Day = kwargs.get('tcmCostHorizon4Day')
        self.__assetClassificationsIsPrimary = kwargs.get('assetClassificationsIsPrimary')
        self.__loanDate = kwargs.get('loanDate')
        self.__styles = kwargs.get('styles')
        self.__lendingSecId = kwargs.get('lendingSecId')
        self.__shortName = kwargs.get('shortName')
        self.__equityTheta = kwargs.get('equityTheta')
        self.__averageFillPrice = kwargs.get('averageFillPrice')
        self.__snowfall = kwargs.get('snowfall')
        self.__mic = kwargs.get('mic')
        self.__bidGspread = kwargs.get('bidGspread')
        self.__openPrice = kwargs.get('openPrice')
        self.__mid = kwargs.get('mid')
        self.__autoExecState = kwargs.get('autoExecState')
        self.__depthSpreadScore = kwargs.get('depthSpreadScore')
        self.__relativeReturnYtd = kwargs.get('relativeReturnYtd')
        self.__long = kwargs.get('long')
        self.__subAccount = kwargs.get('subAccount')
        self.__fairVolatility = kwargs.get('fairVolatility')
        self.__dollarCross = kwargs.get('dollarCross')
        self.__portfolioType = kwargs.get('portfolioType')
        self.__longWeight = kwargs.get('longWeight')
        self.__calculationTime = kwargs.get('calculationTime')
        self.__vendor = kwargs.get('vendor')
        self.__currency = kwargs.get('currency')
        self.__realTimeRestrictionStatus = kwargs.get('realTimeRestrictionStatus')
        self.__averageRealizedVariance = kwargs.get('averageRealizedVariance')
        self.__clusterClass = kwargs.get('clusterClass')
        self.__financialReturnsScore = kwargs.get('financialReturnsScore')
        self.__netChange = kwargs.get('netChange')
        self.__nonSymbolDimensions = kwargs.get('nonSymbolDimensions')
        self.__queueingTime = kwargs.get('queueingTime')
        self.__bidSize = kwargs.get('bidSize')
        self.__swapType = kwargs.get('swapType')
        self.__arrivalMid = kwargs.get('arrivalMid')
        self.__sellSettleDate = kwargs.get('sellSettleDate')
        self.__assetParametersExchangeCurrency = kwargs.get('assetParametersExchangeCurrency')
        self.__unexplained = kwargs.get('unexplained')
        self.__assetClassificationsCountryName = kwargs.get('assetClassificationsCountryName')
        self.__metric = kwargs.get('metric')
        self.__newIdeasYtd = kwargs.get('newIdeasYtd')
        self.__managementFee = kwargs.get('managementFee')
        self.__ask = kwargs.get('ask')
        self.__impliedLognormalVolatility = kwargs.get('impliedLognormalVolatility')
        self.__closePrice = kwargs.get('closePrice')
        self.__endTime = kwargs.get('endTime')
        self.__open = kwargs.get('open')
        self.__sourceId = kwargs.get('sourceId')
        self.__country = kwargs.get('country')
        self.__cusip = kwargs.get('cusip')
        self.__ideaActivityTime = kwargs.get('ideaActivityTime')
        self.__touchSpreadScore = kwargs.get('touchSpreadScore')
        self.__absoluteStrike = kwargs.get('absoluteStrike')
        self.__netExposure = kwargs.get('netExposure')
        self.__source = kwargs.get('source')
        self.__assetClassificationsCountryCode = kwargs.get('assetClassificationsCountryCode')
        self.__frequency = kwargs.get('frequency')
        self.__activityId = kwargs.get('activityId')
        self.__estimatedImpact = kwargs.get('estimatedImpact')
        self.__dataSetSubCategory = kwargs.get('dataSetSubCategory')
        self.__loanSpreadBucket = kwargs.get('loanSpreadBucket')
        self.__assetParametersPricingLocation = kwargs.get('assetParametersPricingLocation')
        self.__eventDescription = kwargs.get('eventDescription')
        self.__strikeReference = kwargs.get('strikeReference')
        self.__details = kwargs.get('details')
        self.__assetCount = kwargs.get('assetCount')
        self.__quantityBucket = kwargs.get('quantityBucket')
        self.__oeName = kwargs.get('oeName')
        self.__given = kwargs.get('given')
        self.__absoluteValue = kwargs.get('absoluteValue')
        self.__delistingDate = kwargs.get('delistingDate')
        self.__longTenor = kwargs.get('longTenor')
        self.__mctr = kwargs.get('mctr')
        self.__weight = kwargs.get('weight')
        self.__historicalClose = kwargs.get('historicalClose')
        self.__assetCountPriced = kwargs.get('assetCountPriced')
        self.__marketDataPoint = kwargs.get('marketDataPoint')
        self.__ideaId = kwargs.get('ideaId')
        self.__commentStatus = kwargs.get('commentStatus')
        self.__marginalCost = kwargs.get('marginalCost')
        self.__absoluteWeight = kwargs.get('absoluteWeight')
        self.__tradeTime = kwargs.get('tradeTime')
        self.__measure = kwargs.get('measure')
        self.__clientWeight = kwargs.get('clientWeight')
        self.__hedgeAnnualizedVolatility = kwargs.get('hedgeAnnualizedVolatility')
        self.__benchmarkCurrency = kwargs.get('benchmarkCurrency')
        self.__name = kwargs.get('name')
        self.__aum = kwargs.get('aum')
        self.__folderName = kwargs.get('folderName')
        self.__lendingPartnerFee = kwargs.get('lendingPartnerFee')
        self.__region = kwargs.get('region')
        self.__liveDate = kwargs.get('liveDate')
        self.__askHigh = kwargs.get('askHigh')
        self.__corporateActionType = kwargs.get('corporateActionType')
        self.__primeId = kwargs.get('primeId')
        self.__tenor2 = kwargs.get('tenor2')
        self.__description = kwargs.get('description')
        self.__valueRevised = kwargs.get('valueRevised')
        self.__ownerName = kwargs.get('ownerName')
        self.__adjustedTradePrice = kwargs.get('adjustedTradePrice')
        self.__lastUpdatedById = kwargs.get('lastUpdatedById')
        self.__zScore = kwargs.get('zScore')
        self.__targetShareholderMeetingDate = kwargs.get('targetShareholderMeetingDate')
        self.__collateralMarketValue = kwargs.get('collateralMarketValue')
        self.__isADR = kwargs.get('isADR')
        self.__eventStartTime = kwargs.get('eventStartTime')
        self.__factor = kwargs.get('factor')
        self.__daysOnLoan = kwargs.get('daysOnLoan')
        self.__longConvictionSmall = kwargs.get('longConvictionSmall')
        self.__serviceId = kwargs.get('serviceId')
        self.__turnover = kwargs.get('turnover')
        self.__complianceEffectiveTime = kwargs.get('complianceEffectiveTime')
        self.__expirationDate = kwargs.get('expirationDate')
        self.__gsfeer = kwargs.get('gsfeer')
        self.__coverage = kwargs.get('coverage')
        self.__backtestId = kwargs.get('backtestId')
        self.__gPercentile = kwargs.get('gPercentile')
        self.__gScore = kwargs.get('gScore')
        self.__marketValue = kwargs.get('marketValue')
        self.__multipleScore = kwargs.get('multipleScore')
        self.__lendingFundNav = kwargs.get('lendingFundNav')
        self.__sourceOriginalCategory = kwargs.get('sourceOriginalCategory')
        self.__betaAdjustedExposure = kwargs.get('betaAdjustedExposure')
        self.__composite5DayAdv = kwargs.get('composite5DayAdv')
        self.__latestExecutionTime = kwargs.get('latestExecutionTime')
        self.__dividendPoints = kwargs.get('dividendPoints')
        self.__newIdeasWtd = kwargs.get('newIdeasWtd')
        self.__paid = kwargs.get('paid')
        self.__short = kwargs.get('short')
        self.__location = kwargs.get('location')
        self.__comment = kwargs.get('comment')
        self.__bosInTicksDescription = kwargs.get('bosInTicksDescription')
        self.__sourceSymbol = kwargs.get('sourceSymbol')
        self.__time = kwargs.get('time')
        self.__scenarioId = kwargs.get('scenarioId')
        self.__askUnadjusted = kwargs.get('askUnadjusted')
        self.__queueClockTime = kwargs.get('queueClockTime')
        self.__askChange = kwargs.get('askChange')
        self.__impliedCorrelation = kwargs.get('impliedCorrelation')
        self.__tcmCostParticipationRate50Pct = kwargs.get('tcmCostParticipationRate50Pct')
        self.__normalizedPerformance = kwargs.get('normalizedPerformance')
        self.__cmId = kwargs.get('cmId')
        self.__type = kwargs.get('type')
        self.__mdapi = kwargs.get('mdapi')
        self.__dividendYield = kwargs.get('dividendYield')
        self.__cumulativePnl = kwargs.get('cumulativePnl')
        self.__sourceOrigin = kwargs.get('sourceOrigin')
        self.__shortTenor = kwargs.get('shortTenor')
        self.__loss = kwargs.get('loss')
        self.__unadjustedVolume = kwargs.get('unadjustedVolume')
        self.__measures = kwargs.get('measures')
        self.__tradingCostPnl = kwargs.get('tradingCostPnl')
        self.__internalUser = kwargs.get('internalUser')
        self.__price = kwargs.get('price')
        self.__paymentQuantity = kwargs.get('paymentQuantity')
        self.__underlyer = kwargs.get('underlyer')
        self.__createdTime = kwargs.get('createdTime')
        self.__positionIdx = kwargs.get('positionIdx')
        self.__secName = kwargs.get('secName')
        self.__percentADV = kwargs.get('percentADV')
        self.__redemptionOption = kwargs.get('redemptionOption')
        self.__unadjustedLow = kwargs.get('unadjustedLow')
        self.__contract = kwargs.get('contract')
        self.__sedol = kwargs.get('sedol')
        self.__roundingCostPnl = kwargs.get('roundingCostPnl')
        self.__sustainGlobal = kwargs.get('sustainGlobal')
        self.__sourceTicker = kwargs.get('sourceTicker')
        self.__portfolioId = kwargs.get('portfolioId')
        self.__gsid = kwargs.get('gsid')
        self.__esPercentile = kwargs.get('esPercentile')
        self.__lendingFund = kwargs.get('lendingFund')
        self.__tcmCostParticipationRate15Pct = kwargs.get('tcmCostParticipationRate15Pct')
        self.__sensitivity = kwargs.get('sensitivity')
        self.__fiscalYear = kwargs.get('fiscalYear')
        self.__recallDate = kwargs.get('recallDate')
        self.__rcic = kwargs.get('rcic')
        self.__simonAssetTags = kwargs.get('simonAssetTags')
        self.__internal = kwargs.get('internal')
        self.__forwardPoint = kwargs.get('forwardPoint')
        self.__assetClassificationsGicsIndustry = kwargs.get('assetClassificationsGicsIndustry')
        self.__adjustedBidPrice = kwargs.get('adjustedBidPrice')
        self.__hitRateQtd = kwargs.get('hitRateQtd')
        self.__varSwap = kwargs.get('varSwap')
        self.__lowUnadjusted = kwargs.get('lowUnadjusted')
        self.__sectorsRaw = kwargs.get('sectorsRaw')
        self.__recallQuantity = kwargs.get('recallQuantity')
        self.__low = kwargs.get('low')
        self.__crossGroup = kwargs.get('crossGroup')
        self.__integratedScore = kwargs.get('integratedScore')
        self.__reportRunTime = kwargs.get('reportRunTime')
        self.__fiveDayPriceChangeBps = kwargs.get('fiveDayPriceChangeBps')
        self.__tradeSize = kwargs.get('tradeSize')
        self.__holdings = kwargs.get('holdings')
        self.__symbolDimensions = kwargs.get('symbolDimensions')
        self.__priceMethod = kwargs.get('priceMethod')
        self.__quotingStyle = kwargs.get('quotingStyle')
        self.__scenarioGroupId = kwargs.get('scenarioGroupId')
        self.__errorMessage = kwargs.get('errorMessage')
        self.__averageImpliedVariance = kwargs.get('averageImpliedVariance')
        self.__avgTradeRateDescription = kwargs.get('avgTradeRateDescription')
        self.__midPrice = kwargs.get('midPrice')
        self.__fraction = kwargs.get('fraction')
        self.__stsCreditMarket = kwargs.get('stsCreditMarket')
        self.__assetCountShort = kwargs.get('assetCountShort')
        self.__stsEmDm = kwargs.get('stsEmDm')
        self.__requiredCollateralValue = kwargs.get('requiredCollateralValue')
        self.__tcmCostHorizon2Day = kwargs.get('tcmCostHorizon2Day')
        self.__pendingLoanCount = kwargs.get('pendingLoanCount')
        self.__queueInLots = kwargs.get('queueInLots')
        self.__priceRangeInTicksDescription = kwargs.get('priceRangeInTicksDescription')
        self.__date = kwargs.get('date')
        self.__tenderOfferExpirationDate = kwargs.get('tenderOfferExpirationDate')
        self.__highUnadjusted = kwargs.get('highUnadjusted')
        self.__sourceCategory = kwargs.get('sourceCategory')
        self.__volumeUnadjusted = kwargs.get('volumeUnadjusted')
        self.__avgTradeRateLabel = kwargs.get('avgTradeRateLabel')
        self.__tcmCostParticipationRate5Pct = kwargs.get('tcmCostParticipationRate5Pct')
        self.__isActive = kwargs.get('isActive')
        self.__growthScore = kwargs.get('growthScore')
        self.__bufferThreshold = kwargs.get('bufferThreshold')
        self.__encodedStats = kwargs.get('encodedStats')
        self.__adjustedShortInterest = kwargs.get('adjustedShortInterest')
        self.__askSize = kwargs.get('askSize')
        self.__mdapiType = kwargs.get('mdapiType')
        self.__group = kwargs.get('group')
        self.__estimatedSpread = kwargs.get('estimatedSpread')
        self.__resource = kwargs.get('resource')
        self.__created = kwargs.get('created')
        self.__averageRealizedVolatility = kwargs.get('averageRealizedVolatility')
        self.__tcmCost = kwargs.get('tcmCost')
        self.__sustainJapan = kwargs.get('sustainJapan')
        self.__navSpread = kwargs.get('navSpread')
        self.__bidPrice = kwargs.get('bidPrice')
        self.__dollarTotalReturn = kwargs.get('dollarTotalReturn')
        self.__hedgeTrackingError = kwargs.get('hedgeTrackingError')
        self.__marketCapCategory = kwargs.get('marketCapCategory')
        self.__historicalVolume = kwargs.get('historicalVolume')
        self.__esNumericPercentile = kwargs.get('esNumericPercentile')
        self.__strikePrice = kwargs.get('strikePrice')
        self.__eventStartDate = kwargs.get('eventStartDate')
        self.__askGspread = kwargs.get('askGspread')
        self.__calSpreadMisPricing = kwargs.get('calSpreadMisPricing')
        self.__equityGamma = kwargs.get('equityGamma')
        self.__grossIncome = kwargs.get('grossIncome')
        self.__emId = kwargs.get('emId')
        self.__adjustedOpenPrice = kwargs.get('adjustedOpenPrice')
        self.__assetCountInModel = kwargs.get('assetCountInModel')
        self.__stsCreditRegion = kwargs.get('stsCreditRegion')
        self.__point = kwargs.get('point')
        self.__totalReturns = kwargs.get('totalReturns')
        self.__lender = kwargs.get('lender')
        self.__minTemperature = kwargs.get('minTemperature')
        self.__closeTime = kwargs.get('closeTime')
        self.__value = kwargs.get('value')
        self.__relativeStrike = kwargs.get('relativeStrike')
        self.__amount = kwargs.get('amount')
        self.__quantity = kwargs.get('quantity')
        self.__lendingFundAcct = kwargs.get('lendingFundAcct')
        self.__reportId = kwargs.get('reportId')
        self.__indexWeight = kwargs.get('indexWeight')
        self.__rebate = kwargs.get('rebate')
        self.__flagship = kwargs.get('flagship')
        self.__trader = kwargs.get('trader')
        self.__factorCategory = kwargs.get('factorCategory')
        self.__impliedVolatility = kwargs.get('impliedVolatility')
        self.__spread = kwargs.get('spread')
        self.__stsRatesMaturity = kwargs.get('stsRatesMaturity')
        self.__equityDelta = kwargs.get('equityDelta')
        self.__grossWeight = kwargs.get('grossWeight')
        self.__listed = kwargs.get('listed')
        self.__variance = kwargs.get('variance')
        self.__tcmCostHorizon6Hour = kwargs.get('tcmCostHorizon6Hour')
        self.__g10Currency = kwargs.get('g10Currency')
        self.__shockStyle = kwargs.get('shockStyle')
        self.__relativePeriod = kwargs.get('relativePeriod')
        self.__isin = kwargs.get('isin')
        self.__methodology = kwargs.get('methodology')

    @property
    def queueClockTimeLabel(self):
        """Label of the Stock's Queue Clock Time  on the particular date."""
        return self.__queueClockTimeLabel

    @queueClockTimeLabel.setter
    def queueClockTimeLabel(self, value):
        self.__queueClockTimeLabel = value
        self._property_changed('queueClockTimeLabel')        

    @property
    def marketPnl(self) -> float:
        """Market Profit and Loss (PNL)."""
        return self.__marketPnl

    @marketPnl.setter
    def marketPnl(self, value: float):
        self.__marketPnl = value
        self._property_changed('marketPnl')        

    @property
    def year(self) -> str:
        """Year of forecast."""
        return self.__year

    @year.setter
    def year(self, value: str):
        self.__year = value
        self._property_changed('year')        

    @property
    def sustainAsiaExJapan(self) -> bool:
        """True if the stock is on the SUSTAIN Asia Ex Japan list as of the corresponding date. False if the stock is removed from the SUSTAIN Asia Ex Japan list on the corresponding date."""
        return self.__sustainAsiaExJapan

    @sustainAsiaExJapan.setter
    def sustainAsiaExJapan(self, value: bool):
        self.__sustainAsiaExJapan = value
        self._property_changed('sustainAsiaExJapan')        

    @property
    def investmentRate(self) -> float:
        """The rate of return on an investment.  In the context of securities lending, it is the rate being earned on the reinvested collateral received from the borrower."""
        return self.__investmentRate

    @investmentRate.setter
    def investmentRate(self, value: float):
        self.__investmentRate = value
        self._property_changed('investmentRate')        

    @property
    def assetClassificationsGicsSubIndustry(self) -> str:
        """GICS Sub Industry classification (level 4)."""
        return self.__assetClassificationsGicsSubIndustry

    @assetClassificationsGicsSubIndustry.setter
    def assetClassificationsGicsSubIndustry(self, value: str):
        self.__assetClassificationsGicsSubIndustry = value
        self._property_changed('assetClassificationsGicsSubIndustry')        

    @property
    def mdapiClass(self) -> str:
        """MDAPI Asset Class."""
        return self.__mdapiClass

    @mdapiClass.setter
    def mdapiClass(self, value: str):
        self.__mdapiClass = value
        self._property_changed('mdapiClass')        

    @property
    def bidUnadjusted(self) -> float:
        """Unadjusted bid level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__bidUnadjusted

    @bidUnadjusted.setter
    def bidUnadjusted(self, value: float):
        self.__bidUnadjusted = value
        self._property_changed('bidUnadjusted')        

    @property
    def economicTermsHash(self) -> str:
        """Hash code for an asset."""
        return self.__economicTermsHash

    @economicTermsHash.setter
    def economicTermsHash(self, value: str):
        self.__economicTermsHash = value
        self._property_changed('economicTermsHash')        

    @property
    def neighbourAssetId(self) -> str:
        """Marquee identifier for the corresponding neighbour."""
        return self.__neighbourAssetId

    @neighbourAssetId.setter
    def neighbourAssetId(self, value: str):
        self.__neighbourAssetId = value
        self._property_changed('neighbourAssetId')        

    @property
    def simonIntlAssetTags(self) -> Tuple[str, ...]:
        """SIMON International Asset Tags."""
        return self.__simonIntlAssetTags

    @simonIntlAssetTags.setter
    def simonIntlAssetTags(self, value: Tuple[str, ...]):
        self.__simonIntlAssetTags = value
        self._property_changed('simonIntlAssetTags')        

    @property
    def path(self) -> str:
        """Path to value."""
        return self.__path

    @path.setter
    def path(self, value: str):
        self.__path = value
        self._property_changed('path')        

    @property
    def availableInventory(self) -> float:
        """An estimated indication of the share quantity potentially available to borrow in the relevant asset."""
        return self.__availableInventory

    @availableInventory.setter
    def availableInventory(self, value: float):
        self.__availableInventory = value
        self._property_changed('availableInventory')        

    @property
    def clientContact(self) -> str:
        """Name of client(s) requesting data."""
        return self.__clientContact

    @clientContact.setter
    def clientContact(self, value: str):
        self.__clientContact = value
        self._property_changed('clientContact')        

    @property
    def est1DayCompletePct(self) -> float:
        """Estimated 1 day completion percentage."""
        return self.__est1DayCompletePct

    @est1DayCompletePct.setter
    def est1DayCompletePct(self, value: float):
        self.__est1DayCompletePct = value
        self._property_changed('est1DayCompletePct')        

    @property
    def rank(self) -> float:
        """Rank to determine most relevant asset."""
        return self.__rank

    @rank.setter
    def rank(self, value: float):
        self.__rank = value
        self._property_changed('rank')        

    @property
    def dataSetCategory(self) -> str:
        """Top level grouping of dataset."""
        return self.__dataSetCategory

    @dataSetCategory.setter
    def dataSetCategory(self, value: str):
        self.__dataSetCategory = value
        self._property_changed('dataSetCategory')        

    @property
    def createdById(self) -> str:
        """Unique identifier of user who created the object"""
        return self.__createdById

    @createdById.setter
    def createdById(self, value: str):
        self.__createdById = value
        self._property_changed('createdById')        

    @property
    def vehicleType(self) -> str:
        """Type of investment vehicle. Only viewable after having been granted additional access to asset information."""
        return self.__vehicleType

    @vehicleType.setter
    def vehicleType(self, value: str):
        self.__vehicleType = value
        self._property_changed('vehicleType')        

    @property
    def dailyRisk(self) -> float:
        """Daily Risk Value."""
        return self.__dailyRisk

    @dailyRisk.setter
    def dailyRisk(self, value: float):
        self.__dailyRisk = value
        self._property_changed('dailyRisk')        

    @property
    def bosInBpsLabel(self):
        """Label of the Stock's Bid-Offer Spread in Basis points on the particular date."""
        return self.__bosInBpsLabel

    @bosInBpsLabel.setter
    def bosInBpsLabel(self, value):
        self.__bosInBpsLabel = value
        self._property_changed('bosInBpsLabel')        

    @property
    def energy(self) -> float:
        """Energy price component."""
        return self.__energy

    @energy.setter
    def energy(self, value: float):
        self.__energy = value
        self._property_changed('energy')        

    @property
    def marketDataType(self) -> str:
        """The market data type (e.g. IR_BASIS, FX_Vol). This can be resolved into a dataset when combined with vendor and intraday=true/false."""
        return self.__marketDataType

    @marketDataType.setter
    def marketDataType(self, value: str):
        self.__marketDataType = value
        self._property_changed('marketDataType')        

    @property
    def sentimentScore(self) -> float:
        """A value representing a sentiment indicator."""
        return self.__sentimentScore

    @sentimentScore.setter
    def sentimentScore(self, value: float):
        self.__sentimentScore = value
        self._property_changed('sentimentScore')        

    @property
    def bosInBps(self) -> float:
        """The Bid-Offer Spread of the stock in Basis points on the particular date."""
        return self.__bosInBps

    @bosInBps.setter
    def bosInBps(self, value: float):
        self.__bosInBps = value
        self._property_changed('bosInBps')        

    @property
    def pointClass(self) -> str:
        """MDAPI Class."""
        return self.__pointClass

    @pointClass.setter
    def pointClass(self, value: str):
        self.__pointClass = value
        self._property_changed('pointClass')        

    @property
    def fxSpot(self) -> float:
        """FX spot rate as determined by fixing source."""
        return self.__fxSpot

    @fxSpot.setter
    def fxSpot(self, value: float):
        self.__fxSpot = value
        self._property_changed('fxSpot')        

    @property
    def bidLow(self) -> float:
        """Lowest Bid Price (price willing to buy)."""
        return self.__bidLow

    @bidLow.setter
    def bidLow(self, value: float):
        self.__bidLow = value
        self._property_changed('bidLow')        

    @property
    def valuePrevious(self) -> str:
        """Value for the previous period after the revision (if revision is applicable)."""
        return self.__valuePrevious

    @valuePrevious.setter
    def valuePrevious(self, value: str):
        self.__valuePrevious = value
        self._property_changed('valuePrevious')        

    @property
    def fairVarianceVolatility(self) -> float:
        """The strike in volatility terms, calculated as square root of fair variance."""
        return self.__fairVarianceVolatility

    @fairVarianceVolatility.setter
    def fairVarianceVolatility(self, value: float):
        self.__fairVarianceVolatility = value
        self._property_changed('fairVarianceVolatility')        

    @property
    def avgTradeRate(self) -> float:
        """The Average Trading Rate of the stock on the particular date."""
        return self.__avgTradeRate

    @avgTradeRate.setter
    def avgTradeRate(self, value: float):
        self.__avgTradeRate = value
        self._property_changed('avgTradeRate')        

    @property
    def shortLevel(self) -> float:
        """Level of the 5-day normalized flow for short selling/covering."""
        return self.__shortLevel

    @shortLevel.setter
    def shortLevel(self, value: float):
        self.__shortLevel = value
        self._property_changed('shortLevel')        

    @property
    def hedgeVolatility(self) -> float:
        """Standard deviation of the annualized returns."""
        return self.__hedgeVolatility

    @hedgeVolatility.setter
    def hedgeVolatility(self, value: float):
        self.__hedgeVolatility = value
        self._property_changed('hedgeVolatility')        

    @property
    def version(self) -> float:
        """Version number."""
        return self.__version

    @version.setter
    def version(self, value: float):
        self.__version = value
        self._property_changed('version')        

    @property
    def tags(self) -> Tuple[str, ...]:
        """Metadata associated with the object"""
        return self.__tags

    @tags.setter
    def tags(self, value: Tuple[str, ...]):
        self.__tags = value
        self._property_changed('tags')        

    @property
    def underlyingAssetId(self) -> str:
        """Marquee identifier for constituents of an index or portfolio."""
        return self.__underlyingAssetId

    @underlyingAssetId.setter
    def underlyingAssetId(self, value: str):
        self.__underlyingAssetId = value
        self._property_changed('underlyingAssetId')        

    @property
    def clientExposure(self) -> float:
        """Exposure of client positions to the factor in percent of equity."""
        return self.__clientExposure

    @clientExposure.setter
    def clientExposure(self, value: float):
        self.__clientExposure = value
        self._property_changed('clientExposure')        

    @property
    def correlation(self) -> float:
        """Market implied correlation between two tenors."""
        return self.__correlation

    @correlation.setter
    def correlation(self, value: float):
        self.__correlation = value
        self._property_changed('correlation')        

    @property
    def exposure(self) -> float:
        """Exposure of a given asset or portfolio in the denominated currency of the asset or portfolio."""
        return self.__exposure

    @exposure.setter
    def exposure(self, value: float):
        self.__exposure = value
        self._property_changed('exposure')        

    @property
    def gsSustainSubSector(self) -> str:
        """GS SUSTAIN sector."""
        return self.__gsSustainSubSector

    @gsSustainSubSector.setter
    def gsSustainSubSector(self, value: str):
        self.__gsSustainSubSector = value
        self._property_changed('gsSustainSubSector')        

    @property
    def domain(self) -> str:
        """Domain that request came from."""
        return self.__domain

    @domain.setter
    def domain(self, value: str):
        self.__domain = value
        self._property_changed('domain')        

    @property
    def marketDataAsset(self) -> str:
        """The market data asset (e.g. USD, USD/EUR)."""
        return self.__marketDataAsset

    @marketDataAsset.setter
    def marketDataAsset(self, value: str):
        self.__marketDataAsset = value
        self._property_changed('marketDataAsset')        

    @property
    def forwardTenor(self) -> str:
        """Start of swap after option expiry."""
        return self.__forwardTenor

    @forwardTenor.setter
    def forwardTenor(self, value: str):
        self.__forwardTenor = value
        self._property_changed('forwardTenor')        

    @property
    def unadjustedHigh(self) -> float:
        """Unadjusted high level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__unadjustedHigh

    @unadjustedHigh.setter
    def unadjustedHigh(self, value: float):
        self.__unadjustedHigh = value
        self._property_changed('unadjustedHigh')        

    @property
    def sourceImportance(self) -> float:
        """Source importance."""
        return self.__sourceImportance

    @sourceImportance.setter
    def sourceImportance(self, value: float):
        self.__sourceImportance = value
        self._property_changed('sourceImportance')        

    @property
    def eid(self) -> str:
        """Goldman Sachs internal exchange identifier."""
        return self.__eid

    @eid.setter
    def eid(self, value: str):
        self.__eid = value
        self._property_changed('eid')        

    @property
    def jsn(self) -> str:
        """Japan security number (subject to licensing)."""
        return self.__jsn

    @jsn.setter
    def jsn(self, value: str):
        self.__jsn = value
        self._property_changed('jsn')        

    @property
    def relativeReturnQtd(self) -> float:
        """Relative Return Quarter to Date."""
        return self.__relativeReturnQtd

    @relativeReturnQtd.setter
    def relativeReturnQtd(self, value: float):
        self.__relativeReturnQtd = value
        self._property_changed('relativeReturnQtd')        

    @property
    def displayName(self) -> str:
        """Display Name."""
        return self.__displayName

    @displayName.setter
    def displayName(self, value: str):
        self.__displayName = value
        self._property_changed('displayName')        

    @property
    def minutesToTrade100Pct(self) -> float:
        """Minutes to trade 100 percent."""
        return self.__minutesToTrade100Pct

    @minutesToTrade100Pct.setter
    def minutesToTrade100Pct(self, value: float):
        self.__minutesToTrade100Pct = value
        self._property_changed('minutesToTrade100Pct')        

    @property
    def marketModelId(self) -> str:
        """Marquee unique market model identifier"""
        return self.__marketModelId

    @marketModelId.setter
    def marketModelId(self, value: str):
        self.__marketModelId = value
        self._property_changed('marketModelId')        

    @property
    def quoteType(self) -> str:
        """Quote Type."""
        return self.__quoteType

    @quoteType.setter
    def quoteType(self, value: str):
        self.__quoteType = value
        self._property_changed('quoteType')        

    @property
    def realizedCorrelation(self) -> float:
        """Correlation of an asset realized by observations of market prices."""
        return self.__realizedCorrelation

    @realizedCorrelation.setter
    def realizedCorrelation(self, value: float):
        self.__realizedCorrelation = value
        self._property_changed('realizedCorrelation')        

    @property
    def tenor(self) -> str:
        """Tenor of instrument."""
        return self.__tenor

    @tenor.setter
    def tenor(self, value: str):
        self.__tenor = value
        self._property_changed('tenor')        

    @property
    def esPolicyPercentile(self) -> float:
        """Sector relative percentile based on E&S policy score."""
        return self.__esPolicyPercentile

    @esPolicyPercentile.setter
    def esPolicyPercentile(self, value: float):
        self.__esPolicyPercentile = value
        self._property_changed('esPolicyPercentile')        

    @property
    def atmFwdRate(self) -> float:
        """ATM forward rate."""
        return self.__atmFwdRate

    @atmFwdRate.setter
    def atmFwdRate(self, value: float):
        self.__atmFwdRate = value
        self._property_changed('atmFwdRate')        

    @property
    def tcmCostParticipationRate75Pct(self) -> float:
        """TCM cost with a 75 percent participation rate."""
        return self.__tcmCostParticipationRate75Pct

    @tcmCostParticipationRate75Pct.setter
    def tcmCostParticipationRate75Pct(self, value: float):
        self.__tcmCostParticipationRate75Pct = value
        self._property_changed('tcmCostParticipationRate75Pct')        

    @property
    def close(self) -> float:
        """Closing level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__close

    @close.setter
    def close(self, value: float):
        self.__close = value
        self._property_changed('close')        

    @property
    def tcmCostParticipationRate100Pct(self) -> float:
        """TCM cost with a 100 percent participation rate."""
        return self.__tcmCostParticipationRate100Pct

    @tcmCostParticipationRate100Pct.setter
    def tcmCostParticipationRate100Pct(self, value: float):
        self.__tcmCostParticipationRate100Pct = value
        self._property_changed('tcmCostParticipationRate100Pct')        

    @property
    def disclaimer(self) -> str:
        """The legal disclaimer associated with the record."""
        return self.__disclaimer

    @disclaimer.setter
    def disclaimer(self, value: str):
        self.__disclaimer = value
        self._property_changed('disclaimer')        

    @property
    def measureIdx(self) -> int:
        """The index of the corresponding measure in the risk request."""
        return self.__measureIdx

    @measureIdx.setter
    def measureIdx(self, value: int):
        self.__measureIdx = value
        self._property_changed('measureIdx')        

    @property
    def a(self) -> float:
        """Stock specific coefficient."""
        return self.__a

    @a.setter
    def a(self, value: float):
        self.__a = value
        self._property_changed('a')        

    @property
    def b(self) -> float:
        """Stock specific coefficient."""
        return self.__b

    @b.setter
    def b(self, value: float):
        self.__b = value
        self._property_changed('b')        

    @property
    def loanFee(self) -> float:
        """Fee charged for the loan of securities to a borrower in a securities lending agreement."""
        return self.__loanFee

    @loanFee.setter
    def loanFee(self, value: float):
        self.__loanFee = value
        self._property_changed('loanFee')        

    @property
    def c(self) -> float:
        """Stock specific coefficient."""
        return self.__c

    @c.setter
    def c(self, value: float):
        self.__c = value
        self._property_changed('c')        

    @property
    def equityVega(self) -> float:
        """Vega exposure to equity products."""
        return self.__equityVega

    @equityVega.setter
    def equityVega(self, value: float):
        self.__equityVega = value
        self._property_changed('equityVega')        

    @property
    def lenderPayment(self) -> float:
        """Payment made to lender's bank in support of the income accrued from securities lending."""
        return self.__lenderPayment

    @lenderPayment.setter
    def lenderPayment(self, value: float):
        self.__lenderPayment = value
        self._property_changed('lenderPayment')        

    @property
    def deploymentVersion(self) -> str:
        """Deployment version."""
        return self.__deploymentVersion

    @deploymentVersion.setter
    def deploymentVersion(self, value: str):
        self.__deploymentVersion = value
        self._property_changed('deploymentVersion')        

    @property
    def fiveDayMove(self) -> float:
        """Five day move in the price."""
        return self.__fiveDayMove

    @fiveDayMove.setter
    def fiveDayMove(self, value: float):
        self.__fiveDayMove = value
        self._property_changed('fiveDayMove')        

    @property
    def borrower(self) -> str:
        """Name of the borrowing entity on a securities lending agreement."""
        return self.__borrower

    @borrower.setter
    def borrower(self, value: str):
        self.__borrower = value
        self._property_changed('borrower')        

    @property
    def valueFormat(self) -> float:
        """Value format."""
        return self.__valueFormat

    @valueFormat.setter
    def valueFormat(self, value: float):
        self.__valueFormat = value
        self._property_changed('valueFormat')        

    @property
    def performanceContribution(self) -> float:
        """The contribution of an underlying asset to the overall performance."""
        return self.__performanceContribution

    @performanceContribution.setter
    def performanceContribution(self, value: float):
        self.__performanceContribution = value
        self._property_changed('performanceContribution')        

    @property
    def targetNotional(self) -> float:
        """Notional value of the hedge target."""
        return self.__targetNotional

    @targetNotional.setter
    def targetNotional(self, value: float):
        self.__targetNotional = value
        self._property_changed('targetNotional')        

    @property
    def fillLegId(self) -> str:
        """Unique identifier for the leg on which the fill executed."""
        return self.__fillLegId

    @fillLegId.setter
    def fillLegId(self, value: str):
        self.__fillLegId = value
        self._property_changed('fillLegId')        

    @property
    def delisted(self) -> str:
        """Whether the security has been delisted."""
        return self.__delisted

    @delisted.setter
    def delisted(self, value: str):
        self.__delisted = value
        self._property_changed('delisted')        

    @property
    def rationale(self) -> str:
        """Reason for changing the status of a trade idea."""
        return self.__rationale

    @rationale.setter
    def rationale(self, value: str):
        self.__rationale = value
        self._property_changed('rationale')        

    @property
    def regionalFocus(self) -> str:
        """Section of the world a fund is focused on from an investment perspective. Same view permissions as the asset."""
        return self.__regionalFocus

    @regionalFocus.setter
    def regionalFocus(self, value: str):
        self.__regionalFocus = value
        self._property_changed('regionalFocus')        

    @property
    def volumePrimary(self) -> float:
        """Accumulated number of shares, lots or contracts traded according to the market convention at the primary exchange."""
        return self.__volumePrimary

    @volumePrimary.setter
    def volumePrimary(self, value: float):
        self.__volumePrimary = value
        self._property_changed('volumePrimary')        

    @property
    def series(self) -> str:
        """Series."""
        return self.__series

    @series.setter
    def series(self, value: str):
        self.__series = value
        self._property_changed('series')        

    @property
    def simonId(self) -> str:
        """SIMON application asset identifier."""
        return self.__simonId

    @simonId.setter
    def simonId(self, value: str):
        self.__simonId = value
        self._property_changed('simonId')        

    @property
    def newIdeasQtd(self) -> float:
        """Ideas received by clients Quarter to date."""
        return self.__newIdeasQtd

    @newIdeasQtd.setter
    def newIdeasQtd(self, value: float):
        self.__newIdeasQtd = value
        self._property_changed('newIdeasQtd')        

    @property
    def congestion(self) -> float:
        """Congestion price component."""
        return self.__congestion

    @congestion.setter
    def congestion(self, value: float):
        self.__congestion = value
        self._property_changed('congestion')        

    @property
    def adjustedAskPrice(self) -> float:
        """Latest Ask Price (price offering to sell) adjusted for corporate actions."""
        return self.__adjustedAskPrice

    @adjustedAskPrice.setter
    def adjustedAskPrice(self, value: float):
        self.__adjustedAskPrice = value
        self._property_changed('adjustedAskPrice')        

    @property
    def quarter(self) -> str:
        """Quarter of forecast."""
        return self.__quarter

    @quarter.setter
    def quarter(self, value: str):
        self.__quarter = value
        self._property_changed('quarter')        

    @property
    def factorUniverse(self) -> str:
        """Factor universe."""
        return self.__factorUniverse

    @factorUniverse.setter
    def factorUniverse(self, value: str):
        self.__factorUniverse = value
        self._property_changed('factorUniverse')        

    @property
    def eventCategory(self) -> str:
        """Category."""
        return self.__eventCategory

    @eventCategory.setter
    def eventCategory(self, value: str):
        self.__eventCategory = value
        self._property_changed('eventCategory')        

    @property
    def impliedNormalVolatility(self) -> float:
        """Market implied volatility measured using a normal model in bps/day."""
        return self.__impliedNormalVolatility

    @impliedNormalVolatility.setter
    def impliedNormalVolatility(self, value: float):
        self.__impliedNormalVolatility = value
        self._property_changed('impliedNormalVolatility')        

    @property
    def unadjustedOpen(self) -> float:
        """Unadjusted open level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__unadjustedOpen

    @unadjustedOpen.setter
    def unadjustedOpen(self, value: float):
        self.__unadjustedOpen = value
        self._property_changed('unadjustedOpen')        

    @property
    def arrivalRt(self) -> float:
        """Arrival Realtime."""
        return self.__arrivalRt

    @arrivalRt.setter
    def arrivalRt(self, value: float):
        self.__arrivalRt = value
        self._property_changed('arrivalRt')        

    @property
    def criticality(self) -> float:
        """The upgrade criticality of a deployment."""
        return self.__criticality

    @criticality.setter
    def criticality(self, value: float):
        self.__criticality = value
        self._property_changed('criticality')        

    @property
    def transactionCost(self) -> float:
        """Transaction cost."""
        return self.__transactionCost

    @transactionCost.setter
    def transactionCost(self, value: float):
        self.__transactionCost = value
        self._property_changed('transactionCost')        

    @property
    def servicingCostShortPnl(self) -> float:
        """Servicing Cost Short Profit and Loss."""
        return self.__servicingCostShortPnl

    @servicingCostShortPnl.setter
    def servicingCostShortPnl(self, value: float):
        self.__servicingCostShortPnl = value
        self._property_changed('servicingCostShortPnl')        

    @property
    def bidAskSpread(self) -> float:
        """Bid ask spread."""
        return self.__bidAskSpread

    @bidAskSpread.setter
    def bidAskSpread(self, value: float):
        self.__bidAskSpread = value
        self._property_changed('bidAskSpread')        

    @property
    def optionType(self) -> str:
        return self.__optionType

    @optionType.setter
    def optionType(self, value: str):
        self.__optionType = value
        self._property_changed('optionType')        

    @property
    def tcmCostHorizon3Hour(self) -> float:
        """TCM cost with a 3 hour time horizon."""
        return self.__tcmCostHorizon3Hour

    @tcmCostHorizon3Hour.setter
    def tcmCostHorizon3Hour(self, value: float):
        self.__tcmCostHorizon3Hour = value
        self._property_changed('tcmCostHorizon3Hour')        

    @property
    def clusterDescription(self) -> str:
        """Description of the Cluster characteristics."""
        return self.__clusterDescription

    @clusterDescription.setter
    def clusterDescription(self, value: str):
        self.__clusterDescription = value
        self._property_changed('clusterDescription')        

    @property
    def creditLimit(self) -> float:
        """The allowed credit limit."""
        return self.__creditLimit

    @creditLimit.setter
    def creditLimit(self, value: float):
        self.__creditLimit = value
        self._property_changed('creditLimit')        

    @property
    def positionAmount(self) -> float:
        """Corporate actions amount * shares."""
        return self.__positionAmount

    @positionAmount.setter
    def positionAmount(self, value: float):
        self.__positionAmount = value
        self._property_changed('positionAmount')        

    @property
    def numberOfPositions(self) -> float:
        """Number of positions."""
        return self.__numberOfPositions

    @numberOfPositions.setter
    def numberOfPositions(self, value: float):
        self.__numberOfPositions = value
        self._property_changed('numberOfPositions')        

    @property
    def windSpeed(self) -> float:
        """Average wind speed in knots."""
        return self.__windSpeed

    @windSpeed.setter
    def windSpeed(self, value: float):
        self.__windSpeed = value
        self._property_changed('windSpeed')        

    @property
    def openUnadjusted(self) -> float:
        """Unadjusted open level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__openUnadjusted

    @openUnadjusted.setter
    def openUnadjusted(self, value: float):
        self.__openUnadjusted = value
        self._property_changed('openUnadjusted')        

    @property
    def maRank(self) -> float:
        """M&A Rank, which may take on the following values: 1 represents high (at least 30%, but less than 50%) probability of the company becoming an acquisition target, 2 represents medium (at least 15%, but less than 30%) probability and 3 represents low (less than 15%) probability."""
        return self.__maRank

    @maRank.setter
    def maRank(self, value: float):
        self.__maRank = value
        self._property_changed('maRank')        

    @property
    def eventStartDateTime(self) -> datetime.datetime:
        """The start time of the event if the event occurs during a time window and the event has a specific start time, using UTC convention (optional)."""
        return self.__eventStartDateTime

    @eventStartDateTime.setter
    def eventStartDateTime(self, value: datetime.datetime):
        self.__eventStartDateTime = value
        self._property_changed('eventStartDateTime')        

    @property
    def askPrice(self) -> float:
        """Latest Ask Price (price offering to sell)."""
        return self.__askPrice

    @askPrice.setter
    def askPrice(self, value: float):
        self.__askPrice = value
        self._property_changed('askPrice')        

    @property
    def eventId(self) -> str:
        """Goldman Sachs internal event identifier."""
        return self.__eventId

    @eventId.setter
    def eventId(self, value: str):
        self.__eventId = value
        self._property_changed('eventId')        

    @property
    def borrowerId(self) -> str:
        """Id of the borrowing entity on a securities lending agreement."""
        return self.__borrowerId

    @borrowerId.setter
    def borrowerId(self, value: str):
        self.__borrowerId = value
        self._property_changed('borrowerId')        

    @property
    def dataProduct(self) -> str:
        """Product that dataset belongs to."""
        return self.__dataProduct

    @dataProduct.setter
    def dataProduct(self, value: str):
        self.__dataProduct = value
        self._property_changed('dataProduct')        

    @property
    def sectors(self) -> Tuple[str, ...]:
        """Sector classifications of an asset."""
        return self.__sectors

    @sectors.setter
    def sectors(self, value: Tuple[str, ...]):
        self.__sectors = value
        self._property_changed('sectors')        

    @property
    def mqSymbol(self) -> str:
        """Goldman Sachs Marquee Symbol applied to entities such as Backtester."""
        return self.__mqSymbol

    @mqSymbol.setter
    def mqSymbol(self, value: str):
        self.__mqSymbol = value
        self._property_changed('mqSymbol')        

    @property
    def annualizedTrackingError(self) -> float:
        """Annualized tracking error."""
        return self.__annualizedTrackingError

    @annualizedTrackingError.setter
    def annualizedTrackingError(self, value: float):
        self.__annualizedTrackingError = value
        self._property_changed('annualizedTrackingError')        

    @property
    def volSwap(self) -> float:
        """The strike in volatility terms, calculated as square root of fair variance."""
        return self.__volSwap

    @volSwap.setter
    def volSwap(self, value: float):
        self.__volSwap = value
        self._property_changed('volSwap')        

    @property
    def annualizedRisk(self) -> float:
        """Annualized risk."""
        return self.__annualizedRisk

    @annualizedRisk.setter
    def annualizedRisk(self, value: float):
        self.__annualizedRisk = value
        self._property_changed('annualizedRisk')        

    @property
    def bmPrimeId(self) -> float:
        """Benchmark prime ID of the treasury."""
        return self.__bmPrimeId

    @bmPrimeId.setter
    def bmPrimeId(self, value: float):
        self.__bmPrimeId = value
        self._property_changed('bmPrimeId')        

    @property
    def corporateAction(self) -> bool:
        """Whether or not it is a corporate action."""
        return self.__corporateAction

    @corporateAction.setter
    def corporateAction(self, value: bool):
        self.__corporateAction = value
        self._property_changed('corporateAction')        

    @property
    def conviction(self) -> str:
        """Confidence level in the trade idea."""
        return self.__conviction

    @conviction.setter
    def conviction(self, value: str):
        self.__conviction = value
        self._property_changed('conviction')        

    @property
    def grossExposure(self) -> float:
        """Sum of absolute long and short exposures in the portfolio. If you are $60 short and $40 long, then the grossExposure would be $100 (60+40)."""
        return self.__grossExposure

    @grossExposure.setter
    def grossExposure(self, value: float):
        self.__grossExposure = value
        self._property_changed('grossExposure')        

    @property
    def benchmarkMaturity(self) -> str:
        """The benchmark tenor."""
        return self.__benchmarkMaturity

    @benchmarkMaturity.setter
    def benchmarkMaturity(self, value: str):
        self.__benchmarkMaturity = value
        self._property_changed('benchmarkMaturity')        

    @property
    def gRegionalScore(self) -> float:
        """A company???s score for G metrics within its region."""
        return self.__gRegionalScore

    @gRegionalScore.setter
    def gRegionalScore(self, value: float):
        self.__gRegionalScore = value
        self._property_changed('gRegionalScore')        

    @property
    def volumeComposite(self) -> float:
        """Accumulated number of shares, lots or contracts traded according to the market convention at all exchanges."""
        return self.__volumeComposite

    @volumeComposite.setter
    def volumeComposite(self, value: float):
        self.__volumeComposite = value
        self._property_changed('volumeComposite')        

    @property
    def volume(self) -> float:
        """Accumulated number of shares, lots or contracts traded according to the market convention."""
        return self.__volume

    @volume.setter
    def volume(self, value: float):
        self.__volume = value
        self._property_changed('volume')        

    @property
    def factorId(self) -> str:
        """Id for Factors."""
        return self.__factorId

    @factorId.setter
    def factorId(self, value: str):
        self.__factorId = value
        self._property_changed('factorId')        

    @property
    def hardToBorrow(self) -> bool:
        """Whether or not an asset is hard to borrow."""
        return self.__hardToBorrow

    @hardToBorrow.setter
    def hardToBorrow(self, value: bool):
        self.__hardToBorrow = value
        self._property_changed('hardToBorrow')        

    @property
    def adv(self) -> float:
        """Average number of shares or units of a given asset traded over a defined period."""
        return self.__adv

    @adv.setter
    def adv(self, value: float):
        self.__adv = value
        self._property_changed('adv')        

    @property
    def stsFxCurrency(self) -> str:
        """Currency of underlying FX risk for STS assets."""
        return self.__stsFxCurrency

    @stsFxCurrency.setter
    def stsFxCurrency(self, value: str):
        self.__stsFxCurrency = value
        self._property_changed('stsFxCurrency')        

    @property
    def wpk(self) -> str:
        """Wertpapierkennnummer (WKN, WPKN, Wert), German security identifier code (subject to licensing)."""
        return self.__wpk

    @wpk.setter
    def wpk(self, value: str):
        self.__wpk = value
        self._property_changed('wpk')        

    @property
    def shortConvictionMedium(self) -> float:
        """The count of short ideas with medium conviction."""
        return self.__shortConvictionMedium

    @shortConvictionMedium.setter
    def shortConvictionMedium(self, value: float):
        self.__shortConvictionMedium = value
        self._property_changed('shortConvictionMedium')        

    @property
    def bidChange(self) -> float:
        """Change in BID price."""
        return self.__bidChange

    @bidChange.setter
    def bidChange(self, value: float):
        self.__bidChange = value
        self._property_changed('bidChange')        

    @property
    def exchange(self) -> str:
        """Name of marketplace where security, derivative or other instrument is traded"""
        return self.__exchange

    @exchange.setter
    def exchange(self, value: str):
        self.__exchange = value
        self._property_changed('exchange')        

    @property
    def expiration(self) -> str:
        """The expiration date of the associated contract and the last date it trades."""
        return self.__expiration

    @expiration.setter
    def expiration(self, value: str):
        self.__expiration = value
        self._property_changed('expiration')        

    @property
    def tradePrice(self) -> float:
        """Last trade price or value."""
        return self.__tradePrice

    @tradePrice.setter
    def tradePrice(self, value: float):
        self.__tradePrice = value
        self._property_changed('tradePrice')        

    @property
    def esPolicyScore(self) -> float:
        """Score for E&S policy metrics."""
        return self.__esPolicyScore

    @esPolicyScore.setter
    def esPolicyScore(self, value: float):
        self.__esPolicyScore = value
        self._property_changed('esPolicyScore')        

    @property
    def loanId(self) -> str:
        """Loan reference for a securities lending loan."""
        return self.__loanId

    @loanId.setter
    def loanId(self, value: str):
        self.__loanId = value
        self._property_changed('loanId')        

    @property
    def primeIdNumeric(self) -> float:
        """Prime ID as a number."""
        return self.__primeIdNumeric

    @primeIdNumeric.setter
    def primeIdNumeric(self, value: float):
        self.__primeIdNumeric = value
        self._property_changed('primeIdNumeric')        

    @property
    def cid(self) -> str:
        """Goldman Sachs internal company identifier."""
        return self.__cid

    @cid.setter
    def cid(self, value: str):
        self.__cid = value
        self._property_changed('cid')        

    @property
    def onboarded(self) -> bool:
        """Whether or not social domain has been onboarded."""
        return self.__onboarded

    @onboarded.setter
    def onboarded(self, value: bool):
        self.__onboarded = value
        self._property_changed('onboarded')        

    @property
    def liquidityScore(self) -> float:
        """Liquidity conditions in the aggregate market, calculated as the average of touch liquidity score, touch spread score, and depth spread score."""
        return self.__liquidityScore

    @liquidityScore.setter
    def liquidityScore(self, value: float):
        self.__liquidityScore = value
        self._property_changed('liquidityScore')        

    @property
    def importance(self) -> float:
        """Importance."""
        return self.__importance

    @importance.setter
    def importance(self, value: float):
        self.__importance = value
        self._property_changed('importance')        

    @property
    def sourceDateSpan(self) -> float:
        """Date span for event in days."""
        return self.__sourceDateSpan

    @sourceDateSpan.setter
    def sourceDateSpan(self, value: float):
        self.__sourceDateSpan = value
        self._property_changed('sourceDateSpan')        

    @property
    def assetClassificationsGicsSector(self) -> str:
        """GICS Sector classification (level 1)."""
        return self.__assetClassificationsGicsSector

    @assetClassificationsGicsSector.setter
    def assetClassificationsGicsSector(self, value: str):
        self.__assetClassificationsGicsSector = value
        self._property_changed('assetClassificationsGicsSector')        

    @property
    def underlyingDataSetId(self) -> str:
        """Dataset on which this (virtual) dataset is based."""
        return self.__underlyingDataSetId

    @underlyingDataSetId.setter
    def underlyingDataSetId(self, value: str):
        self.__underlyingDataSetId = value
        self._property_changed('underlyingDataSetId')        

    @property
    def stsAssetName(self) -> str:
        """Name of risk asset for STS underliers."""
        return self.__stsAssetName

    @stsAssetName.setter
    def stsAssetName(self, value: str):
        self.__stsAssetName = value
        self._property_changed('stsAssetName')        

    @property
    def closeUnadjusted(self) -> float:
        """Unadjusted Close level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__closeUnadjusted

    @closeUnadjusted.setter
    def closeUnadjusted(self, value: float):
        self.__closeUnadjusted = value
        self._property_changed('closeUnadjusted')        

    @property
    def valueUnit(self) -> str:
        """Value unit."""
        return self.__valueUnit

    @valueUnit.setter
    def valueUnit(self, value: str):
        self.__valueUnit = value
        self._property_changed('valueUnit')        

    @property
    def bidHigh(self) -> float:
        """The highest bid (price willing to buy)."""
        return self.__bidHigh

    @bidHigh.setter
    def bidHigh(self, value: float):
        self.__bidHigh = value
        self._property_changed('bidHigh')        

    @property
    def adjustedLowPrice(self) -> float:
        """Adjusted low level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__adjustedLowPrice

    @adjustedLowPrice.setter
    def adjustedLowPrice(self, value: float):
        self.__adjustedLowPrice = value
        self._property_changed('adjustedLowPrice')        

    @property
    def netExposureClassification(self) -> str:
        """Classification for net exposure of fund."""
        return self.__netExposureClassification

    @netExposureClassification.setter
    def netExposureClassification(self, value: str):
        self.__netExposureClassification = value
        self._property_changed('netExposureClassification')        

    @property
    def longConvictionLarge(self) -> float:
        """The count of long ideas with large conviction."""
        return self.__longConvictionLarge

    @longConvictionLarge.setter
    def longConvictionLarge(self, value: float):
        self.__longConvictionLarge = value
        self._property_changed('longConvictionLarge')        

    @property
    def fairVariance(self) -> float:
        """Strike such that the price of an uncapped variance swap on the underlying index is zero at inception."""
        return self.__fairVariance

    @fairVariance.setter
    def fairVariance(self, value: float):
        self.__fairVariance = value
        self._property_changed('fairVariance')        

    @property
    def hitRateWtd(self) -> float:
        """Hit Rate Ratio Week to Date."""
        return self.__hitRateWtd

    @hitRateWtd.setter
    def hitRateWtd(self, value: float):
        self.__hitRateWtd = value
        self._property_changed('hitRateWtd')        

    @property
    def oad(self) -> float:
        """Option-adjusted duration."""
        return self.__oad

    @oad.setter
    def oad(self, value: float):
        self.__oad = value
        self._property_changed('oad')        

    @property
    def bosInBpsDescription(self) -> str:
        """Description of the Stock's Bid-Offer Spread in Basis points on the particular date."""
        return self.__bosInBpsDescription

    @bosInBpsDescription.setter
    def bosInBpsDescription(self, value: str):
        self.__bosInBpsDescription = value
        self._property_changed('bosInBpsDescription')        

    @property
    def lowPrice(self) -> float:
        """Low level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__lowPrice

    @lowPrice.setter
    def lowPrice(self, value: float):
        self.__lowPrice = value
        self._property_changed('lowPrice')        

    @property
    def realizedVolatility(self) -> float:
        """Volatility of an asset realized by observations of market prices."""
        return self.__realizedVolatility

    @realizedVolatility.setter
    def realizedVolatility(self, value: float):
        self.__realizedVolatility = value
        self._property_changed('realizedVolatility')        

    @property
    def rate(self) -> float:
        """Rate of the asset for the time period in percent."""
        return self.__rate

    @rate.setter
    def rate(self, value: float):
        self.__rate = value
        self._property_changed('rate')        

    @property
    def adv22DayPct(self) -> float:
        """Median number of shares or units of a given asset traded over a 21 day period."""
        return self.__adv22DayPct

    @adv22DayPct.setter
    def adv22DayPct(self, value: float):
        self.__adv22DayPct = value
        self._property_changed('adv22DayPct')        

    @property
    def alpha(self) -> float:
        """Alpha."""
        return self.__alpha

    @alpha.setter
    def alpha(self, value: float):
        self.__alpha = value
        self._property_changed('alpha')        

    @property
    def client(self) -> str:
        """Entity name."""
        return self.__client

    @client.setter
    def client(self, value: str):
        self.__client = value
        self._property_changed('client')        

    @property
    def cloneParentId(self) -> str:
        """Marquee unique identifier"""
        return self.__cloneParentId

    @cloneParentId.setter
    def cloneParentId(self, value: str):
        self.__cloneParentId = value
        self._property_changed('cloneParentId')        

    @property
    def company(self) -> str:
        """Activity user company."""
        return self.__company

    @company.setter
    def company(self, value: str):
        self.__company = value
        self._property_changed('company')        

    @property
    def convictionList(self) -> bool:
        """Conviction List, which is true if the security is on the Conviction Buy List or false otherwise. Securities with a convictionList value equal to true are by definition a subset of the securities with a rating equal to Buy."""
        return self.__convictionList

    @convictionList.setter
    def convictionList(self, value: bool):
        self.__convictionList = value
        self._property_changed('convictionList')        

    @property
    def priceRangeInTicksLabel(self):
        """Label of the Stock's Price Range in Ticks on the particular date."""
        return self.__priceRangeInTicksLabel

    @priceRangeInTicksLabel.setter
    def priceRangeInTicksLabel(self, value):
        self.__priceRangeInTicksLabel = value
        self._property_changed('priceRangeInTicksLabel')        

    @property
    def ticker(self) -> str:
        """Ticker."""
        return self.__ticker

    @ticker.setter
    def ticker(self, value: str):
        self.__ticker = value
        self._property_changed('ticker')        

    @property
    def inRiskModel(self) -> bool:
        """Whether or not the asset is in the risk model universe."""
        return self.__inRiskModel

    @inRiskModel.setter
    def inRiskModel(self, value: bool):
        self.__inRiskModel = value
        self._property_changed('inRiskModel')        

    @property
    def tcmCostHorizon1Day(self) -> float:
        """TCM cost with a 1 day time horizon."""
        return self.__tcmCostHorizon1Day

    @tcmCostHorizon1Day.setter
    def tcmCostHorizon1Day(self, value: float):
        self.__tcmCostHorizon1Day = value
        self._property_changed('tcmCostHorizon1Day')        

    @property
    def servicingCostLongPnl(self) -> float:
        """Servicing Cost Long Profit and Loss."""
        return self.__servicingCostLongPnl

    @servicingCostLongPnl.setter
    def servicingCostLongPnl(self, value: float):
        self.__servicingCostLongPnl = value
        self._property_changed('servicingCostLongPnl')        

    @property
    def stsRatesCountry(self) -> str:
        """Country of interest rate risk for STS assets."""
        return self.__stsRatesCountry

    @stsRatesCountry.setter
    def stsRatesCountry(self, value: str):
        self.__stsRatesCountry = value
        self._property_changed('stsRatesCountry')        

    @property
    def meetingNumber(self) -> float:
        """Central bank meeting number."""
        return self.__meetingNumber

    @meetingNumber.setter
    def meetingNumber(self, value: float):
        self.__meetingNumber = value
        self._property_changed('meetingNumber')        

    @property
    def exchangeId(self) -> str:
        """Unique identifier for an exchange."""
        return self.__exchangeId

    @exchangeId.setter
    def exchangeId(self, value: str):
        self.__exchangeId = value
        self._property_changed('exchangeId')        

    @property
    def horizon(self) -> str:
        """Time period indicating the validity of the idea. Eg. 2d (2 days), 1w (1 week), 3m (3 months), 1y (1 year)."""
        return self.__horizon

    @horizon.setter
    def horizon(self, value: str):
        self.__horizon = value
        self._property_changed('horizon')        

    @property
    def midGspread(self) -> float:
        """Mid G spread."""
        return self.__midGspread

    @midGspread.setter
    def midGspread(self, value: float):
        self.__midGspread = value
        self._property_changed('midGspread')        

    @property
    def tcmCostHorizon20Day(self) -> float:
        """TCM cost with a 20 day time horizon."""
        return self.__tcmCostHorizon20Day

    @tcmCostHorizon20Day.setter
    def tcmCostHorizon20Day(self, value: float):
        self.__tcmCostHorizon20Day = value
        self._property_changed('tcmCostHorizon20Day')        

    @property
    def longLevel(self) -> float:
        """Level of the 5-day normalized flow for long selling/buying."""
        return self.__longLevel

    @longLevel.setter
    def longLevel(self, value: float):
        self.__longLevel = value
        self._property_changed('longLevel')        

    @property
    def sourceValueForecast(self) -> str:
        """TE own projections."""
        return self.__sourceValueForecast

    @sourceValueForecast.setter
    def sourceValueForecast(self, value: str):
        self.__sourceValueForecast = value
        self._property_changed('sourceValueForecast')        

    @property
    def shortConvictionLarge(self) -> float:
        """The count of short ideas with large conviction."""
        return self.__shortConvictionLarge

    @shortConvictionLarge.setter
    def shortConvictionLarge(self, value: float):
        self.__shortConvictionLarge = value
        self._property_changed('shortConvictionLarge')        

    @property
    def realm(self) -> str:
        """Realm."""
        return self.__realm

    @realm.setter
    def realm(self, value: str):
        self.__realm = value
        self._property_changed('realm')        

    @property
    def bid(self) -> float:
        """Latest Bid Price (price willing to buy)."""
        return self.__bid

    @bid.setter
    def bid(self, value: float):
        self.__bid = value
        self._property_changed('bid')        

    @property
    def dataDescription(self) -> str:
        """Description of data that client is requesting."""
        return self.__dataDescription

    @dataDescription.setter
    def dataDescription(self, value: str):
        self.__dataDescription = value
        self._property_changed('dataDescription')        

    @property
    def counterPartyStatus(self) -> str:
        """The lending status of a counterparty for a particular portfolio."""
        return self.__counterPartyStatus

    @counterPartyStatus.setter
    def counterPartyStatus(self, value: str):
        self.__counterPartyStatus = value
        self._property_changed('counterPartyStatus')        

    @property
    def composite22DayAdv(self) -> float:
        """Composite 22 day ADV."""
        return self.__composite22DayAdv

    @composite22DayAdv.setter
    def composite22DayAdv(self, value: float):
        self.__composite22DayAdv = value
        self._property_changed('composite22DayAdv')        

    @property
    def dollarExcessReturn(self) -> float:
        """The dollar excess return of an instrument."""
        return self.__dollarExcessReturn

    @dollarExcessReturn.setter
    def dollarExcessReturn(self, value: float):
        self.__dollarExcessReturn = value
        self._property_changed('dollarExcessReturn')        

    @property
    def gsn(self) -> str:
        """Goldman Sachs internal product number."""
        return self.__gsn

    @gsn.setter
    def gsn(self, value: str):
        self.__gsn = value
        self._property_changed('gsn')        

    @property
    def isAggressive(self) -> float:
        """Indicates if the fill was aggressive or passive."""
        return self.__isAggressive

    @isAggressive.setter
    def isAggressive(self, value: float):
        self.__isAggressive = value
        self._property_changed('isAggressive')        

    @property
    def tradeEndDate(self) -> datetime.date:
        """End date of the trade."""
        return self.__tradeEndDate

    @tradeEndDate.setter
    def tradeEndDate(self, value: datetime.date):
        self.__tradeEndDate = value
        self._property_changed('tradeEndDate')        

    @property
    def orderId(self) -> str:
        """The unique ID of the order."""
        return self.__orderId

    @orderId.setter
    def orderId(self, value: str):
        self.__orderId = value
        self._property_changed('orderId')        

    @property
    def gss(self) -> str:
        """Goldman Sachs internal product symbol."""
        return self.__gss

    @gss.setter
    def gss(self, value: str):
        self.__gss = value
        self._property_changed('gss')        

    @property
    def percentOfMediandv1m(self) -> float:
        """Percentage of median daily volume calculated using 1 month period (last 22 trading days)."""
        return self.__percentOfMediandv1m

    @percentOfMediandv1m.setter
    def percentOfMediandv1m(self, value: float):
        self.__percentOfMediandv1m = value
        self._property_changed('percentOfMediandv1m')        

    @property
    def lendables(self) -> float:
        """Market value of holdings available to a securities lending program for lending."""
        return self.__lendables

    @lendables.setter
    def lendables(self, value: float):
        self.__lendables = value
        self._property_changed('lendables')        

    @property
    def assetClass(self) -> str:
        """Asset classification of security. Assets are classified into broad groups which exhibit similar characteristics and behave in a consistent way under different market conditions"""
        return self.__assetClass

    @assetClass.setter
    def assetClass(self, value: str):
        self.__assetClass = value
        self._property_changed('assetClass')        

    @property
    def gsideid(self) -> str:
        """Goldman Sachs internal composite equity and exchange identifier."""
        return self.__gsideid

    @gsideid.setter
    def gsideid(self, value: str):
        self.__gsideid = value
        self._property_changed('gsideid')        

    @property
    def bosInTicksLabel(self):
        """Label of the Stock's Bid-Offer Spread in Ticks on the particular date."""
        return self.__bosInTicksLabel

    @bosInTicksLabel.setter
    def bosInTicksLabel(self, value):
        self.__bosInTicksLabel = value
        self._property_changed('bosInTicksLabel')        

    @property
    def ric(self) -> str:
        """Reuters instrument code (subject to licensing)."""
        return self.__ric

    @ric.setter
    def ric(self, value: str):
        self.__ric = value
        self._property_changed('ric')        

    @property
    def positionSourceId(self) -> str:
        """Marquee unique identifier"""
        return self.__positionSourceId

    @positionSourceId.setter
    def positionSourceId(self, value: str):
        self.__positionSourceId = value
        self._property_changed('positionSourceId')        

    @property
    def division(self) -> str:
        """Division that owns the data."""
        return self.__division

    @division.setter
    def division(self, value: str):
        self.__division = value
        self._property_changed('division')        

    @property
    def marketCapUSD(self) -> float:
        """Market capitalization of a given asset denominated in USD."""
        return self.__marketCapUSD

    @marketCapUSD.setter
    def marketCapUSD(self, value: float):
        self.__marketCapUSD = value
        self._property_changed('marketCapUSD')        

    @property
    def gsSustainRegion(self) -> str:
        """Region assigned by GIR ESG SUSTAIN team."""
        return self.__gsSustainRegion

    @gsSustainRegion.setter
    def gsSustainRegion(self, value: str):
        self.__gsSustainRegion = value
        self._property_changed('gsSustainRegion')        

    @property
    def deploymentId(self) -> float:
        """Deployment ID."""
        return self.__deploymentId

    @deploymentId.setter
    def deploymentId(self, value: float):
        self.__deploymentId = value
        self._property_changed('deploymentId')        

    @property
    def highPrice(self) -> float:
        """High level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__highPrice

    @highPrice.setter
    def highPrice(self, value: float):
        self.__highPrice = value
        self._property_changed('highPrice')        

    @property
    def loanStatus(self) -> str:
        """Notes which point of the lifecyle a securities lending loan is in."""
        return self.__loanStatus

    @loanStatus.setter
    def loanStatus(self, value: str):
        self.__loanStatus = value
        self._property_changed('loanStatus')        

    @property
    def shortWeight(self) -> float:
        """Short weight of a position in a given portfolio. Equivalent to position short exposure / total short exposure. If you have a position with a shortExposure of $20, and your portfolio shortExposure is $100, then your asset shortWeight would be 0.2 (20/100)."""
        return self.__shortWeight

    @shortWeight.setter
    def shortWeight(self, value: float):
        self.__shortWeight = value
        self._property_changed('shortWeight')        

    @property
    def absoluteShares(self) -> float:
        """The number of shares without adjusting for side."""
        return self.__absoluteShares

    @absoluteShares.setter
    def absoluteShares(self, value: float):
        self.__absoluteShares = value
        self._property_changed('absoluteShares')        

    @property
    def action(self) -> str:
        """The activity action. For example: Viewed"""
        return self.__action

    @action.setter
    def action(self, value: str):
        self.__action = value
        self._property_changed('action')        

    @property
    def model(self) -> str:
        """Model."""
        return self.__model

    @model.setter
    def model(self, value: str):
        self.__model = value
        self._property_changed('model')        

    @property
    def id(self) -> str:
        """Marquee unique identifier"""
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = value
        self._property_changed('id')        

    @property
    def arrivalHaircutVwapNormalized(self) -> float:
        """Performance against Benchmark in pip."""
        return self.__arrivalHaircutVwapNormalized

    @arrivalHaircutVwapNormalized.setter
    def arrivalHaircutVwapNormalized(self, value: float):
        self.__arrivalHaircutVwapNormalized = value
        self._property_changed('arrivalHaircutVwapNormalized')        

    @property
    def priceComponent(self) -> str:
        """Component of total price."""
        return self.__priceComponent

    @priceComponent.setter
    def priceComponent(self, value: str):
        self.__priceComponent = value
        self._property_changed('priceComponent')        

    @property
    def queueClockTimeDescription(self) -> str:
        """Description of the Stock's Queue Clock Time on the particular date."""
        return self.__queueClockTimeDescription

    @queueClockTimeDescription.setter
    def queueClockTimeDescription(self, value: str):
        self.__queueClockTimeDescription = value
        self._property_changed('queueClockTimeDescription')        

    @property
    def loanRebate(self) -> float:
        """Rebate paid back to a securities lending borrower."""
        return self.__loanRebate

    @loanRebate.setter
    def loanRebate(self, value: float):
        self.__loanRebate = value
        self._property_changed('loanRebate')        

    @property
    def period(self) -> str:
        """Period for the relevant metric, such as 12MF (12 Months Forward)."""
        return self.__period

    @period.setter
    def period(self, value: str):
        self.__period = value
        self._property_changed('period')        

    @property
    def indexCreateSource(self) -> str:
        """Source of basket create"""
        return self.__indexCreateSource

    @indexCreateSource.setter
    def indexCreateSource(self, value: str):
        self.__indexCreateSource = value
        self._property_changed('indexCreateSource')        

    @property
    def fiscalQuarter(self) -> str:
        """One of the four three-month periods that make up the fiscal year."""
        return self.__fiscalQuarter

    @fiscalQuarter.setter
    def fiscalQuarter(self, value: str):
        self.__fiscalQuarter = value
        self._property_changed('fiscalQuarter')        

    @property
    def deltaStrike(self) -> str:
        """Option strike price expressed in terms of delta * 100."""
        return self.__deltaStrike

    @deltaStrike.setter
    def deltaStrike(self, value: str):
        self.__deltaStrike = value
        self._property_changed('deltaStrike')        

    @property
    def marketImpact(self) -> float:
        """Market impact is based on the Goldman Sachs Shortfall Model where available alongside best estimates from the desk."""
        return self.__marketImpact

    @marketImpact.setter
    def marketImpact(self, value: float):
        self.__marketImpact = value
        self._property_changed('marketImpact')        

    @property
    def eventType(self) -> str:
        """Equals Analyst Meeting if the event indicates an analyst meeting. Equals Earnings Release if the event indicates an earnings release. Equals Sales Release when the event indicates a sales release. Indicates Drug Data when the event indicates an event related to drugs data. Equals Other for any other events."""
        return self.__eventType

    @eventType.setter
    def eventType(self, value: str):
        self.__eventType = value
        self._property_changed('eventType')        

    @property
    def assetCountLong(self) -> float:
        """Number of assets in a portfolio with long exposure."""
        return self.__assetCountLong

    @assetCountLong.setter
    def assetCountLong(self, value: float):
        self.__assetCountLong = value
        self._property_changed('assetCountLong')        

    @property
    def valueActual(self) -> str:
        """Latest released value."""
        return self.__valueActual

    @valueActual.setter
    def valueActual(self, value: str):
        self.__valueActual = value
        self._property_changed('valueActual')        

    @property
    def bcid(self) -> str:
        """Bloomberg composite identifier (ticker and country code)."""
        return self.__bcid

    @bcid.setter
    def bcid(self, value: str):
        self.__bcid = value
        self._property_changed('bcid')        

    @property
    def collateralCurrency(self) -> str:
        """Currency, ISO 4217 currency code or exchange quote modifier (e.g. GBP vs GBp)"""
        return self.__collateralCurrency

    @collateralCurrency.setter
    def collateralCurrency(self, value: str):
        self.__collateralCurrency = value
        self._property_changed('collateralCurrency')        

    @property
    def restrictionStartDate(self) -> datetime.date:
        """The date at which the security restriction was enacted."""
        return self.__restrictionStartDate

    @restrictionStartDate.setter
    def restrictionStartDate(self, value: datetime.date):
        self.__restrictionStartDate = value
        self._property_changed('restrictionStartDate')        

    @property
    def originalCountry(self) -> str:
        """Country in source dataset."""
        return self.__originalCountry

    @originalCountry.setter
    def originalCountry(self, value: str):
        self.__originalCountry = value
        self._property_changed('originalCountry')        

    @property
    def touchLiquidityScore(self) -> float:
        """Z-score of the amount available to trade at the top of the aggregated order book."""
        return self.__touchLiquidityScore

    @touchLiquidityScore.setter
    def touchLiquidityScore(self, value: float):
        self.__touchLiquidityScore = value
        self._property_changed('touchLiquidityScore')        

    @property
    def field(self) -> str:
        """The market data field (e.g. rate, price). This can be resolved into a dataset when combined with vendor and intraday=true/false."""
        return self.__field

    @field.setter
    def field(self, value: str):
        self.__field = value
        self._property_changed('field')        

    @property
    def factorCategoryId(self) -> str:
        """Id for Factor Categories."""
        return self.__factorCategoryId

    @factorCategoryId.setter
    def factorCategoryId(self, value: str):
        self.__factorCategoryId = value
        self._property_changed('factorCategoryId')        

    @property
    def spot(self) -> float:
        """Spot price."""
        return self.__spot

    @spot.setter
    def spot(self, value: float):
        self.__spot = value
        self._property_changed('spot')        

    @property
    def expectedCompletionDate(self) -> str:
        """Expected day of acquisition completion."""
        return self.__expectedCompletionDate

    @expectedCompletionDate.setter
    def expectedCompletionDate(self, value: str):
        self.__expectedCompletionDate = value
        self._property_changed('expectedCompletionDate')        

    @property
    def loanValue(self) -> float:
        return self.__loanValue

    @loanValue.setter
    def loanValue(self, value: float):
        self.__loanValue = value
        self._property_changed('loanValue')        

    @property
    def tradingRestriction(self) -> bool:
        """Whether or not the asset has trading restrictions."""
        return self.__tradingRestriction

    @tradingRestriction.setter
    def tradingRestriction(self, value: bool):
        self.__tradingRestriction = value
        self._property_changed('tradingRestriction')        

    @property
    def skew(self) -> float:
        """Volatility skew."""
        return self.__skew

    @skew.setter
    def skew(self, value: float):
        self.__skew = value
        self._property_changed('skew')        

    @property
    def status(self) -> str:
        """Status of report run"""
        return self.__status

    @status.setter
    def status(self, value: str):
        self.__status = value
        self._property_changed('status')        

    @property
    def sustainEmergingMarkets(self) -> bool:
        """True if the stock is on the SUSTAIN Emerging Markets list as of the corresponding date. False if the stock is removed from the SUSTAIN Emerging Markets list on the corresponding date."""
        return self.__sustainEmergingMarkets

    @sustainEmergingMarkets.setter
    def sustainEmergingMarkets(self, value: bool):
        self.__sustainEmergingMarkets = value
        self._property_changed('sustainEmergingMarkets')        

    @property
    def eventDateTime(self) -> datetime.datetime:
        """The time of the event if the event has a specific time, using UTC convention, or the end time of the event if the event occurs during a time window (optional)."""
        return self.__eventDateTime

    @eventDateTime.setter
    def eventDateTime(self, value: datetime.datetime):
        self.__eventDateTime = value
        self._property_changed('eventDateTime')        

    @property
    def totalReturnPrice(self) -> float:
        """The total return price of an instrument."""
        return self.__totalReturnPrice

    @totalReturnPrice.setter
    def totalReturnPrice(self, value: float):
        self.__totalReturnPrice = value
        self._property_changed('totalReturnPrice')        

    @property
    def city(self) -> str:
        """City for which the weather data was gathered."""
        return self.__city

    @city.setter
    def city(self, value: str):
        self.__city = value
        self._property_changed('city')        

    @property
    def totalPrice(self) -> float:
        """Net price of the asset."""
        return self.__totalPrice

    @totalPrice.setter
    def totalPrice(self, value: float):
        self.__totalPrice = value
        self._property_changed('totalPrice')        

    @property
    def eventSource(self) -> str:
        """Equals GS if the event is sourced from Goldman Sachs Global Investment Research analysts. Equals TR if the event is sourced from Refinitive StreetEvents."""
        return self.__eventSource

    @eventSource.setter
    def eventSource(self, value: str):
        self.__eventSource = value
        self._property_changed('eventSource')        

    @property
    def qisPermNo(self) -> str:
        """QIS Permanent Security Number."""
        return self.__qisPermNo

    @qisPermNo.setter
    def qisPermNo(self, value: str):
        self.__qisPermNo = value
        self._property_changed('qisPermNo')        

    @property
    def hitRateYtd(self) -> float:
        """Hit Rate Ratio Year to Date."""
        return self.__hitRateYtd

    @hitRateYtd.setter
    def hitRateYtd(self, value: float):
        self.__hitRateYtd = value
        self._property_changed('hitRateYtd')        

    @property
    def valid(self) -> float:
        """Valid."""
        return self.__valid

    @valid.setter
    def valid(self, value: float):
        self.__valid = value
        self._property_changed('valid')        

    @property
    def stsCommodity(self) -> str:
        """Commodity name for STS assets."""
        return self.__stsCommodity

    @stsCommodity.setter
    def stsCommodity(self, value: str):
        self.__stsCommodity = value
        self._property_changed('stsCommodity')        

    @property
    def stsCommoditySector(self) -> str:
        """Commodity sector for STS assets."""
        return self.__stsCommoditySector

    @stsCommoditySector.setter
    def stsCommoditySector(self, value: str):
        self.__stsCommoditySector = value
        self._property_changed('stsCommoditySector')        

    @property
    def exceptionStatus(self) -> str:
        """The violation status for this particular line item."""
        return self.__exceptionStatus

    @exceptionStatus.setter
    def exceptionStatus(self, value: str):
        self.__exceptionStatus = value
        self._property_changed('exceptionStatus')        

    @property
    def salesCoverage(self) -> str:
        """Primary or secondary sales coverage."""
        return self.__salesCoverage

    @salesCoverage.setter
    def salesCoverage(self, value: str):
        self.__salesCoverage = value
        self._property_changed('salesCoverage')        

    @property
    def shortExposure(self) -> float:
        """Exposure of a given portfolio to securities which are short in direction. If you are $60 short and $40 long, shortExposure would be $60."""
        return self.__shortExposure

    @shortExposure.setter
    def shortExposure(self, value: float):
        self.__shortExposure = value
        self._property_changed('shortExposure')        

    @property
    def esScore(self) -> float:
        """E&S numeric score + E&S policy score."""
        return self.__esScore

    @esScore.setter
    def esScore(self, value: float):
        self.__esScore = value
        self._property_changed('esScore')        

    @property
    def tcmCostParticipationRate10Pct(self) -> float:
        """TCM cost with a 10 percent participation rate."""
        return self.__tcmCostParticipationRate10Pct

    @tcmCostParticipationRate10Pct.setter
    def tcmCostParticipationRate10Pct(self, value: float):
        self.__tcmCostParticipationRate10Pct = value
        self._property_changed('tcmCostParticipationRate10Pct')        

    @property
    def eventTime(self) -> str:
        """The time of the event if the event has a specific time or the end time of the event if the event occurs during a time window (optional). It is represented in HH:MM 24 hour format in the time zone of the exchange where the company is listed."""
        return self.__eventTime

    @eventTime.setter
    def eventTime(self, value: str):
        self.__eventTime = value
        self._property_changed('eventTime')        

    @property
    def positionSourceName(self) -> str:
        """Position source name for quick access."""
        return self.__positionSourceName

    @positionSourceName.setter
    def positionSourceName(self, value: str):
        self.__positionSourceName = value
        self._property_changed('positionSourceName')        

    @property
    def priceRangeInTicks(self) -> float:
        """The Price Range of the stock in Ticks on the particular date."""
        return self.__priceRangeInTicks

    @priceRangeInTicks.setter
    def priceRangeInTicks(self, value: float):
        self.__priceRangeInTicks = value
        self._property_changed('priceRangeInTicks')        

    @property
    def deliveryDate(self) -> datetime.date:
        """The final date by which the underlying commodity for a futures contract must be delivered in order for the terms of the contract to be fulfilled."""
        return self.__deliveryDate

    @deliveryDate.setter
    def deliveryDate(self, value: datetime.date):
        self.__deliveryDate = value
        self._property_changed('deliveryDate')        

    @property
    def arrivalHaircutVwap(self) -> float:
        """Arrival Haircut VWAP."""
        return self.__arrivalHaircutVwap

    @arrivalHaircutVwap.setter
    def arrivalHaircutVwap(self, value: float):
        self.__arrivalHaircutVwap = value
        self._property_changed('arrivalHaircutVwap')        

    @property
    def interestRate(self) -> float:
        """Interest rate."""
        return self.__interestRate

    @interestRate.setter
    def interestRate(self, value: float):
        self.__interestRate = value
        self._property_changed('interestRate')        

    @property
    def executionDays(self) -> float:
        """Number of days to used to execute."""
        return self.__executionDays

    @executionDays.setter
    def executionDays(self, value: float):
        self.__executionDays = value
        self._property_changed('executionDays')        

    @property
    def recallDueDate(self) -> datetime.date:
        """Date in which the recall of securities in a stock loan recall activity must be complete."""
        return self.__recallDueDate

    @recallDueDate.setter
    def recallDueDate(self, value: datetime.date):
        self.__recallDueDate = value
        self._property_changed('recallDueDate')        

    @property
    def pctChange(self) -> float:
        """Percentage change of the latest trade price or value from the adjusted historical close."""
        return self.__pctChange

    @pctChange.setter
    def pctChange(self, value: float):
        self.__pctChange = value
        self._property_changed('pctChange')        

    @property
    def side(self) -> str:
        """Long or short."""
        return self.__side

    @side.setter
    def side(self, value: str):
        self.__side = value
        self._property_changed('side')        

    @property
    def numberOfRolls(self) -> int:
        """Contract's number of rolls per year."""
        return self.__numberOfRolls

    @numberOfRolls.setter
    def numberOfRolls(self, value: int):
        self.__numberOfRolls = value
        self._property_changed('numberOfRolls')        

    @property
    def agentLenderFee(self) -> float:
        """Fee earned by the Agent Lender for facilitating a securities lending agreement."""
        return self.__agentLenderFee

    @agentLenderFee.setter
    def agentLenderFee(self, value: float):
        self.__agentLenderFee = value
        self._property_changed('agentLenderFee')        

    @property
    def complianceRestrictedStatus(self) -> str:
        """Restricted status as set by compliance."""
        return self.__complianceRestrictedStatus

    @complianceRestrictedStatus.setter
    def complianceRestrictedStatus(self, value: str):
        self.__complianceRestrictedStatus = value
        self._property_changed('complianceRestrictedStatus')        

    @property
    def forward(self) -> float:
        """Forward value."""
        return self.__forward

    @forward.setter
    def forward(self, value: float):
        self.__forward = value
        self._property_changed('forward')        

    @property
    def borrowFee(self) -> float:
        """An indication of the rate one would be charged for borrowing/shorting the relevant asset on that day, expressed in annualized percent terms. Rates may change daily."""
        return self.__borrowFee

    @borrowFee.setter
    def borrowFee(self, value: float):
        self.__borrowFee = value
        self._property_changed('borrowFee')        

    @property
    def strike(self) -> float:
        """Strike level relative to at the money in basis points."""
        return self.__strike

    @strike.setter
    def strike(self, value: float):
        self.__strike = value
        self._property_changed('strike')        

    @property
    def updateTime(self) -> datetime.datetime:
        """Update time of the data element, which allows historical as-of query."""
        return self.__updateTime

    @updateTime.setter
    def updateTime(self, value: datetime.datetime):
        self.__updateTime = value
        self._property_changed('updateTime')        

    @property
    def loanSpread(self) -> float:
        """The difference between the investment rate on cash collateral and the rebate rate of a loan."""
        return self.__loanSpread

    @loanSpread.setter
    def loanSpread(self, value: float):
        self.__loanSpread = value
        self._property_changed('loanSpread')        

    @property
    def tcmCostHorizon12Hour(self) -> float:
        """TCM cost with a 12 hour time horizon."""
        return self.__tcmCostHorizon12Hour

    @tcmCostHorizon12Hour.setter
    def tcmCostHorizon12Hour(self, value: float):
        self.__tcmCostHorizon12Hour = value
        self._property_changed('tcmCostHorizon12Hour')        

    @property
    def dewPoint(self) -> float:
        """Temperature in fahrenheit below which water condenses."""
        return self.__dewPoint

    @dewPoint.setter
    def dewPoint(self, value: float):
        self.__dewPoint = value
        self._property_changed('dewPoint')        

    @property
    def researchCommission(self) -> float:
        """The dollar amount of commissions received from clients."""
        return self.__researchCommission

    @researchCommission.setter
    def researchCommission(self, value: float):
        self.__researchCommission = value
        self._property_changed('researchCommission')        

    @property
    def bbid(self) -> str:
        """Bloomberg identifier (ticker and exchange code)."""
        return self.__bbid

    @bbid.setter
    def bbid(self, value: str):
        self.__bbid = value
        self._property_changed('bbid')        

    @property
    def assetClassificationsRiskCountryCode(self) -> str:
        """Risk Country code (ISO 3166)."""
        return self.__assetClassificationsRiskCountryCode

    @assetClassificationsRiskCountryCode.setter
    def assetClassificationsRiskCountryCode(self, value: str):
        self.__assetClassificationsRiskCountryCode = value
        self._property_changed('assetClassificationsRiskCountryCode')        

    @property
    def eventStatus(self) -> str:
        """Included if there is additional information about an event, such as the event being cancelled."""
        return self.__eventStatus

    @eventStatus.setter
    def eventStatus(self, value: str):
        self.__eventStatus = value
        self._property_changed('eventStatus')        

    @property
    def sellDate(self) -> datetime.date:
        """Sell date of the securities triggering the stock loan recall activity."""
        return self.__sellDate

    @sellDate.setter
    def sellDate(self, value: datetime.date):
        self.__sellDate = value
        self._property_changed('sellDate')        

    @property
    def effectiveDate(self) -> datetime.date:
        """The date at which the measure becomes effective."""
        return self.__effectiveDate

    @effectiveDate.setter
    def effectiveDate(self, value: datetime.date):
        self.__effectiveDate = value
        self._property_changed('effectiveDate')        

    @property
    def return_(self) -> float:
        """Return of asset over a given period (e.g. close-to-close)."""
        return self.__return

    @return_.setter
    def return_(self, value: float):
        self.__return = value
        self._property_changed('return')        

    @property
    def maxTemperature(self) -> float:
        """Maximum temperature observed on a given day in fahrenheit."""
        return self.__maxTemperature

    @maxTemperature.setter
    def maxTemperature(self, value: float):
        self.__maxTemperature = value
        self._property_changed('maxTemperature')        

    @property
    def acquirerShareholderMeetingDate(self) -> str:
        """Shareholders meeting date for acquiring entity."""
        return self.__acquirerShareholderMeetingDate

    @acquirerShareholderMeetingDate.setter
    def acquirerShareholderMeetingDate(self, value: str):
        self.__acquirerShareholderMeetingDate = value
        self._property_changed('acquirerShareholderMeetingDate')        

    @property
    def arrivalMidNormalized(self) -> float:
        """Performance against Benchmark in pip."""
        return self.__arrivalMidNormalized

    @arrivalMidNormalized.setter
    def arrivalMidNormalized(self, value: float):
        self.__arrivalMidNormalized = value
        self._property_changed('arrivalMidNormalized')        

    @property
    def rating(self) -> str:
        """Analyst Rating, which may take on the following values."""
        return self.__rating

    @rating.setter
    def rating(self, value: str):
        self.__rating = value
        self._property_changed('rating')        

    @property
    def volatility(self) -> float:
        """Market implied correlation between two tenors."""
        return self.__volatility

    @volatility.setter
    def volatility(self, value: float):
        self.__volatility = value
        self._property_changed('volatility')        

    @property
    def arrivalRtNormalized(self) -> float:
        """Performance against Benchmark in pip."""
        return self.__arrivalRtNormalized

    @arrivalRtNormalized.setter
    def arrivalRtNormalized(self, value: float):
        self.__arrivalRtNormalized = value
        self._property_changed('arrivalRtNormalized')        

    @property
    def performanceFee(self) -> Union[float, Op]:
        return self.__performanceFee

    @performanceFee.setter
    def performanceFee(self, value: Union[float, Op]):
        self.__performanceFee = value
        self._property_changed('performanceFee')        

    @property
    def reportType(self) -> str:
        """Type of report to execute"""
        return self.__reportType

    @reportType.setter
    def reportType(self, value: str):
        self.__reportType = value
        self._property_changed('reportType')        

    @property
    def sourceURL(self) -> str:
        """Source URL."""
        return self.__sourceURL

    @sourceURL.setter
    def sourceURL(self, value: str):
        self.__sourceURL = value
        self._property_changed('sourceURL')        

    @property
    def estimatedReturn(self) -> float:
        """Estimated return of asset over a given period (e.g. close-to-close)."""
        return self.__estimatedReturn

    @estimatedReturn.setter
    def estimatedReturn(self, value: float):
        self.__estimatedReturn = value
        self._property_changed('estimatedReturn')        

    @property
    def underlyingAssetIds(self) -> Tuple[str, ...]:
        """Marquee IDs of the underlying assets."""
        return self.__underlyingAssetIds

    @underlyingAssetIds.setter
    def underlyingAssetIds(self, value: Tuple[str, ...]):
        self.__underlyingAssetIds = value
        self._property_changed('underlyingAssetIds')        

    @property
    def high(self) -> float:
        """High level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__high

    @high.setter
    def high(self, value: float):
        self.__high = value
        self._property_changed('high')        

    @property
    def sourceLastUpdate(self) -> str:
        """Source last update."""
        return self.__sourceLastUpdate

    @sourceLastUpdate.setter
    def sourceLastUpdate(self, value: str):
        self.__sourceLastUpdate = value
        self._property_changed('sourceLastUpdate')        

    @property
    def queueInLotsLabel(self):
        """Label of the Stock's Queue size in Lots (if applicable) on the particular date."""
        return self.__queueInLotsLabel

    @queueInLotsLabel.setter
    def queueInLotsLabel(self, value):
        self.__queueInLotsLabel = value
        self._property_changed('queueInLotsLabel')        

    @property
    def adv10DayPct(self) -> float:
        """Median number of shares or units of a given asset traded over a 10 day period."""
        return self.__adv10DayPct

    @adv10DayPct.setter
    def adv10DayPct(self, value: float):
        self.__adv10DayPct = value
        self._property_changed('adv10DayPct')        

    @property
    def longConvictionMedium(self) -> float:
        """The count of long ideas with medium conviction."""
        return self.__longConvictionMedium

    @longConvictionMedium.setter
    def longConvictionMedium(self, value: float):
        self.__longConvictionMedium = value
        self._property_changed('longConvictionMedium')        

    @property
    def eventName(self) -> str:
        """Event name."""
        return self.__eventName

    @eventName.setter
    def eventName(self, value: str):
        self.__eventName = value
        self._property_changed('eventName')        

    @property
    def annualRisk(self) -> float:
        """Annualized risk of a given portfolio, position or asset. Generally computed as annualized daily standard deviation of returns."""
        return self.__annualRisk

    @annualRisk.setter
    def annualRisk(self, value: float):
        self.__annualRisk = value
        self._property_changed('annualRisk')        

    @property
    def eti(self) -> str:
        """External Trade Identifier."""
        return self.__eti

    @eti.setter
    def eti(self, value: str):
        self.__eti = value
        self._property_changed('eti')        

    @property
    def dailyTrackingError(self) -> float:
        """Daily tracking error."""
        return self.__dailyTrackingError

    @dailyTrackingError.setter
    def dailyTrackingError(self, value: float):
        self.__dailyTrackingError = value
        self._property_changed('dailyTrackingError')        

    @property
    def unadjustedBid(self) -> float:
        """Unadjusted bid level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__unadjustedBid

    @unadjustedBid.setter
    def unadjustedBid(self, value: float):
        self.__unadjustedBid = value
        self._property_changed('unadjustedBid')        

    @property
    def gsdeer(self) -> float:
        """Goldman Sachs Dynamic Equilibrium Exchange Rate."""
        return self.__gsdeer

    @gsdeer.setter
    def gsdeer(self, value: float):
        self.__gsdeer = value
        self._property_changed('gsdeer')        

    @property
    def gRegionalPercentile(self) -> float:
        """A percentile that captures a company???s G ranking relative to its region."""
        return self.__gRegionalPercentile

    @gRegionalPercentile.setter
    def gRegionalPercentile(self, value: float):
        self.__gRegionalPercentile = value
        self._property_changed('gRegionalPercentile')        

    @property
    def marketBuffer(self) -> float:
        """The actual buffer between holdings and on loan quantity for a market."""
        return self.__marketBuffer

    @marketBuffer.setter
    def marketBuffer(self, value: float):
        self.__marketBuffer = value
        self._property_changed('marketBuffer')        

    @property
    def marketCap(self) -> float:
        """Market capitalization of a given asset in denominated currency."""
        return self.__marketCap

    @marketCap.setter
    def marketCap(self, value: float):
        self.__marketCap = value
        self._property_changed('marketCap')        

    @property
    def oeId(self) -> str:
        """Marquee unique identifier"""
        return self.__oeId

    @oeId.setter
    def oeId(self, value: str):
        self.__oeId = value
        self._property_changed('oeId')        

    @property
    def clusterRegion(self):
        """The cluster region the stock belongs to."""
        return self.__clusterRegion

    @clusterRegion.setter
    def clusterRegion(self, value):
        self.__clusterRegion = value
        self._property_changed('clusterRegion')        

    @property
    def bbidEquivalent(self) -> str:
        """Bloomberg identifier (ticker and country code) equivalent - i.e. for OTCs options, the equivalent BBID on exchange."""
        return self.__bbidEquivalent

    @bbidEquivalent.setter
    def bbidEquivalent(self, value: str):
        self.__bbidEquivalent = value
        self._property_changed('bbidEquivalent')        

    @property
    def prevCloseAsk(self) -> float:
        """Previous business day's close ask price."""
        return self.__prevCloseAsk

    @prevCloseAsk.setter
    def prevCloseAsk(self, value: float):
        self.__prevCloseAsk = value
        self._property_changed('prevCloseAsk')        

    @property
    def level(self) -> float:
        """Level of the 5-day normalized flow in a given factor."""
        return self.__level

    @level.setter
    def level(self, value: float):
        self.__level = value
        self._property_changed('level')        

    @property
    def valoren(self) -> str:
        """Valoren or VALOR number, Swiss primary security identifier (subject to licensing)."""
        return self.__valoren

    @valoren.setter
    def valoren(self, value: str):
        self.__valoren = value
        self._property_changed('valoren')        

    @property
    def esMomentumScore(self) -> float:
        """A company???s score for E&S momentum."""
        return self.__esMomentumScore

    @esMomentumScore.setter
    def esMomentumScore(self, value: float):
        self.__esMomentumScore = value
        self._property_changed('esMomentumScore')        

    @property
    def pressure(self) -> float:
        """Average barometric pressure on a given day in inches of mercury."""
        return self.__pressure

    @pressure.setter
    def pressure(self, value: float):
        self.__pressure = value
        self._property_changed('pressure')        

    @property
    def shortDescription(self) -> str:
        """Short description of dataset."""
        return self.__shortDescription

    @shortDescription.setter
    def shortDescription(self, value: str):
        self.__shortDescription = value
        self._property_changed('shortDescription')        

    @property
    def basis(self) -> float:
        """Spread to be added to the shorter tenor leg for the swap to be ATM."""
        return self.__basis

    @basis.setter
    def basis(self, value: float):
        self.__basis = value
        self._property_changed('basis')        

    @property
    def netWeight(self) -> float:
        """Difference between the longWeight and shortWeight. If you have IBM stock with shortWeight 0.2 and also IBM stock with longWeight 0.4, then the netWeight would be 0.2 (-0.2+0.4)."""
        return self.__netWeight

    @netWeight.setter
    def netWeight(self, value: float):
        self.__netWeight = value
        self._property_changed('netWeight')        

    @property
    def hedgeId(self) -> str:
        """Marquee unique identifier for a hedge."""
        return self.__hedgeId

    @hedgeId.setter
    def hedgeId(self, value: str):
        self.__hedgeId = value
        self._property_changed('hedgeId')        

    @property
    def portfolioManagers(self) -> Tuple[str, ...]:
        """Portfolio managers of asset."""
        return self.__portfolioManagers

    @portfolioManagers.setter
    def portfolioManagers(self, value: Tuple[str, ...]):
        self.__portfolioManagers = value
        self._property_changed('portfolioManagers')        

    @property
    def assetParametersCommoditySector(self) -> str:
        """The sector of the commodity"""
        return self.__assetParametersCommoditySector

    @assetParametersCommoditySector.setter
    def assetParametersCommoditySector(self, value: str):
        self.__assetParametersCommoditySector = value
        self._property_changed('assetParametersCommoditySector')        

    @property
    def bosInTicks(self) -> float:
        """The Bid-Offer Spread of the stock in Ticks on the particular date."""
        return self.__bosInTicks

    @bosInTicks.setter
    def bosInTicks(self, value: float):
        self.__bosInTicks = value
        self._property_changed('bosInTicks')        

    @property
    def tcmCostHorizon8Day(self) -> float:
        """TCM cost with a 8 day time horizon."""
        return self.__tcmCostHorizon8Day

    @tcmCostHorizon8Day.setter
    def tcmCostHorizon8Day(self, value: float):
        self.__tcmCostHorizon8Day = value
        self._property_changed('tcmCostHorizon8Day')        

    @property
    def supraStrategy(self) -> str:
        """Broad descriptor of a fund's investment approach. Same view permissions as the asset"""
        return self.__supraStrategy

    @supraStrategy.setter
    def supraStrategy(self, value: str):
        self.__supraStrategy = value
        self._property_changed('supraStrategy')        

    @property
    def marketBufferThreshold(self) -> float:
        """The required buffer between holdings and on loan quantity for a market."""
        return self.__marketBufferThreshold

    @marketBufferThreshold.setter
    def marketBufferThreshold(self, value: float):
        self.__marketBufferThreshold = value
        self._property_changed('marketBufferThreshold')        

    @property
    def adv5DayPct(self) -> float:
        """Median number of shares or units of a given asset traded over a 5 day period."""
        return self.__adv5DayPct

    @adv5DayPct.setter
    def adv5DayPct(self, value: float):
        self.__adv5DayPct = value
        self._property_changed('adv5DayPct')        

    @property
    def factorSource(self) -> str:
        """Factor source. One of: Axioma, Prime."""
        return self.__factorSource

    @factorSource.setter
    def factorSource(self, value: str):
        self.__factorSource = value
        self._property_changed('factorSource')        

    @property
    def leverage(self) -> float:
        """Leverage."""
        return self.__leverage

    @leverage.setter
    def leverage(self, value: float):
        self.__leverage = value
        self._property_changed('leverage')        

    @property
    def submitter(self) -> str:
        """Name of person submitting request."""
        return self.__submitter

    @submitter.setter
    def submitter(self, value: str):
        self.__submitter = value
        self._property_changed('submitter')        

    @property
    def notional(self) -> float:
        """Notional."""
        return self.__notional

    @notional.setter
    def notional(self, value: float):
        self.__notional = value
        self._property_changed('notional')        

    @property
    def esDisclosurePercentage(self) -> float:
        """Percentage of E&S metrics disclosed by the company."""
        return self.__esDisclosurePercentage

    @esDisclosurePercentage.setter
    def esDisclosurePercentage(self, value: float):
        self.__esDisclosurePercentage = value
        self._property_changed('esDisclosurePercentage')        

    @property
    def investmentIncome(self) -> float:
        return self.__investmentIncome

    @investmentIncome.setter
    def investmentIncome(self, value: float):
        self.__investmentIncome = value
        self._property_changed('investmentIncome')        

    @property
    def clientShortName(self) -> str:
        """The short name of a client."""
        return self.__clientShortName

    @clientShortName.setter
    def clientShortName(self, value: str):
        self.__clientShortName = value
        self._property_changed('clientShortName')        

    @property
    def fwdPoints(self) -> float:
        """Forward points."""
        return self.__fwdPoints

    @fwdPoints.setter
    def fwdPoints(self, value: float):
        self.__fwdPoints = value
        self._property_changed('fwdPoints')        

    @property
    def groupCategory(self) -> str:
        """The type of group: region or sector."""
        return self.__groupCategory

    @groupCategory.setter
    def groupCategory(self, value: str):
        self.__groupCategory = value
        self._property_changed('groupCategory')        

    @property
    def kpiId(self) -> str:
        """Marquee unique KPI identifier."""
        return self.__kpiId

    @kpiId.setter
    def kpiId(self, value: str):
        self.__kpiId = value
        self._property_changed('kpiId')        

    @property
    def relativeReturnWtd(self) -> float:
        """Relative Return Week to Date."""
        return self.__relativeReturnWtd

    @relativeReturnWtd.setter
    def relativeReturnWtd(self, value: float):
        self.__relativeReturnWtd = value
        self._property_changed('relativeReturnWtd')        

    @property
    def bidPlusAsk(self) -> float:
        """Sum of bid & ask."""
        return self.__bidPlusAsk

    @bidPlusAsk.setter
    def bidPlusAsk(self, value: float):
        self.__bidPlusAsk = value
        self._property_changed('bidPlusAsk')        

    @property
    def borrowCost(self) -> float:
        """An indication of the rate one would be charged for borrowing/shorting the relevant asset on that day, expressed in bps. Rates may change daily."""
        return self.__borrowCost

    @borrowCost.setter
    def borrowCost(self, value: float):
        self.__borrowCost = value
        self._property_changed('borrowCost')        

    @property
    def assetClassificationsRiskCountryName(self) -> str:
        """Risk country."""
        return self.__assetClassificationsRiskCountryName

    @assetClassificationsRiskCountryName.setter
    def assetClassificationsRiskCountryName(self, value: str):
        self.__assetClassificationsRiskCountryName = value
        self._property_changed('assetClassificationsRiskCountryName')        

    @property
    def total(self) -> float:
        """Total exposure."""
        return self.__total

    @total.setter
    def total(self, value: float):
        self.__total = value
        self._property_changed('total')        

    @property
    def riskModel(self) -> str:
        """Model used to compute risk or performance attribution. Defines universe, factors, calibration period etc."""
        return self.__riskModel

    @riskModel.setter
    def riskModel(self, value: str):
        self.__riskModel = value
        self._property_changed('riskModel')        

    @property
    def assetId(self) -> str:
        """Marquee unique asset identifier."""
        return self.__assetId

    @assetId.setter
    def assetId(self, value: str):
        self.__assetId = value
        self._property_changed('assetId')        

    @property
    def averageImpliedVolatility(self) -> float:
        """Average volatility of an asset implied by observations of market prices."""
        return self.__averageImpliedVolatility

    @averageImpliedVolatility.setter
    def averageImpliedVolatility(self, value: float):
        self.__averageImpliedVolatility = value
        self._property_changed('averageImpliedVolatility')        

    @property
    def lastUpdatedTime(self) -> datetime.datetime:
        """Timestamp of when the object was last updated"""
        return self.__lastUpdatedTime

    @lastUpdatedTime.setter
    def lastUpdatedTime(self, value: datetime.datetime):
        self.__lastUpdatedTime = value
        self._property_changed('lastUpdatedTime')        

    @property
    def fairValue(self) -> float:
        """Fair Value."""
        return self.__fairValue

    @fairValue.setter
    def fairValue(self, value: float):
        self.__fairValue = value
        self._property_changed('fairValue')        

    @property
    def adjustedHighPrice(self) -> float:
        """Adjusted high level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__adjustedHighPrice

    @adjustedHighPrice.setter
    def adjustedHighPrice(self, value: float):
        self.__adjustedHighPrice = value
        self._property_changed('adjustedHighPrice')        

    @property
    def openTime(self) -> datetime.datetime:
        """Time opened. ISO 8601 formatted string."""
        return self.__openTime

    @openTime.setter
    def openTime(self, value: datetime.datetime):
        self.__openTime = value
        self._property_changed('openTime')        

    @property
    def beta(self) -> float:
        """Beta."""
        return self.__beta

    @beta.setter
    def beta(self, value: float):
        self.__beta = value
        self._property_changed('beta')        

    @property
    def direction(self) -> str:
        """Indicates whether exposure of a given position is long or short."""
        return self.__direction

    @direction.setter
    def direction(self, value: str):
        self.__direction = value
        self._property_changed('direction')        

    @property
    def valueForecast(self) -> str:
        """Average forecast among a representative group of economists."""
        return self.__valueForecast

    @valueForecast.setter
    def valueForecast(self, value: str):
        self.__valueForecast = value
        self._property_changed('valueForecast')        

    @property
    def longExposure(self) -> float:
        """Exposure of a given portfolio to securities which are long in direction. If you are $60 short and $40 long, longExposure would be $40."""
        return self.__longExposure

    @longExposure.setter
    def longExposure(self, value: float):
        self.__longExposure = value
        self._property_changed('longExposure')        

    @property
    def positionSourceType(self) -> str:
        """Source object for position data"""
        return self.__positionSourceType

    @positionSourceType.setter
    def positionSourceType(self, value: str):
        self.__positionSourceType = value
        self._property_changed('positionSourceType')        

    @property
    def tcmCostParticipationRate20Pct(self) -> float:
        """TCM cost with a 20 percent participation rate."""
        return self.__tcmCostParticipationRate20Pct

    @tcmCostParticipationRate20Pct.setter
    def tcmCostParticipationRate20Pct(self, value: float):
        self.__tcmCostParticipationRate20Pct = value
        self._property_changed('tcmCostParticipationRate20Pct')        

    @property
    def adjustedClosePrice(self) -> float:
        """Closing Price adjusted for corporate actions."""
        return self.__adjustedClosePrice

    @adjustedClosePrice.setter
    def adjustedClosePrice(self, value: float):
        self.__adjustedClosePrice = value
        self._property_changed('adjustedClosePrice')        

    @property
    def cross(self) -> str:
        """FX cross symbol."""
        return self.__cross

    @cross.setter
    def cross(self, value: str):
        self.__cross = value
        self._property_changed('cross')        

    @property
    def lmsId(self) -> str:
        """Market identifier code."""
        return self.__lmsId

    @lmsId.setter
    def lmsId(self, value: str):
        self.__lmsId = value
        self._property_changed('lmsId')        

    @property
    def rebateRate(self) -> float:
        """Defines the rate of the cash-back payment to an investor who puts up collateral in borrowing a stock. A rebate rate of interest implies a fee for the loan of securities."""
        return self.__rebateRate

    @rebateRate.setter
    def rebateRate(self, value: float):
        self.__rebateRate = value
        self._property_changed('rebateRate')        

    @property
    def ideaStatus(self) -> str:
        """The activity status of the idea."""
        return self.__ideaStatus

    @ideaStatus.setter
    def ideaStatus(self, value: str):
        self.__ideaStatus = value
        self._property_changed('ideaStatus')        

    @property
    def participationRate(self) -> float:
        """Executed quantity over market volume (e.g. 5, 10, 20)."""
        return self.__participationRate

    @participationRate.setter
    def participationRate(self, value: float):
        self.__participationRate = value
        self._property_changed('participationRate')        

    @property
    def obfr(self) -> float:
        """The overnight bank funding rate."""
        return self.__obfr

    @obfr.setter
    def obfr(self, value: float):
        self.__obfr = value
        self._property_changed('obfr')        

    @property
    def fxForecast(self) -> float:
        """FX forecast value for the relative period."""
        return self.__fxForecast

    @fxForecast.setter
    def fxForecast(self, value: float):
        self.__fxForecast = value
        self._property_changed('fxForecast')        

    @property
    def fixingTimeLabel(self) -> str:
        """Time at which the fixing was taken."""
        return self.__fixingTimeLabel

    @fixingTimeLabel.setter
    def fixingTimeLabel(self, value: str):
        self.__fixingTimeLabel = value
        self._property_changed('fixingTimeLabel')        

    @property
    def implementationId(self) -> str:
        """Marquee unique Implementation identifier."""
        return self.__implementationId

    @implementationId.setter
    def implementationId(self, value: str):
        self.__implementationId = value
        self._property_changed('implementationId')        

    @property
    def fillId(self) -> str:
        """Unique identifier for a fill."""
        return self.__fillId

    @fillId.setter
    def fillId(self, value: str):
        self.__fillId = value
        self._property_changed('fillId')        

    @property
    def excessReturns(self) -> float:
        """Excess returns for backtest."""
        return self.__excessReturns

    @excessReturns.setter
    def excessReturns(self, value: float):
        self.__excessReturns = value
        self._property_changed('excessReturns')        

    @property
    def esMomentumPercentile(self) -> float:
        """A percentile that captures a company???s E&S momentum ranking within its subsector."""
        return self.__esMomentumPercentile

    @esMomentumPercentile.setter
    def esMomentumPercentile(self, value: float):
        self.__esMomentumPercentile = value
        self._property_changed('esMomentumPercentile')        

    @property
    def dollarReturn(self) -> float:
        """Dollar return of asset over a given period (e.g. close-to-close)."""
        return self.__dollarReturn

    @dollarReturn.setter
    def dollarReturn(self, value: float):
        self.__dollarReturn = value
        self._property_changed('dollarReturn')        

    @property
    def esNumericScore(self) -> float:
        """Score for E&S numeric metrics."""
        return self.__esNumericScore

    @esNumericScore.setter
    def esNumericScore(self, value: float):
        self.__esNumericScore = value
        self._property_changed('esNumericScore')        

    @property
    def lenderIncomeAdjustment(self) -> float:
        """Adjustments to income earned by the Lender for the loan of securities to a borrower."""
        return self.__lenderIncomeAdjustment

    @lenderIncomeAdjustment.setter
    def lenderIncomeAdjustment(self, value: float):
        self.__lenderIncomeAdjustment = value
        self._property_changed('lenderIncomeAdjustment')        

    @property
    def inBenchmark(self) -> bool:
        """Whether or not the asset is in the benchmark."""
        return self.__inBenchmark

    @inBenchmark.setter
    def inBenchmark(self, value: bool):
        self.__inBenchmark = value
        self._property_changed('inBenchmark')        

    @property
    def strategy(self) -> str:
        """More specific descriptor of a fund's investment approach. Same view permissions as the asset."""
        return self.__strategy

    @strategy.setter
    def strategy(self, value: str):
        self.__strategy = value
        self._property_changed('strategy')        

    @property
    def positionType(self) -> str:
        """Type of positions."""
        return self.__positionType

    @positionType.setter
    def positionType(self, value: str):
        self.__positionType = value
        self._property_changed('positionType')        

    @property
    def lenderIncome(self) -> float:
        """Income earned by the Lender for the loan of securities to a borrower."""
        return self.__lenderIncome

    @lenderIncome.setter
    def lenderIncome(self, value: float):
        self.__lenderIncome = value
        self._property_changed('lenderIncome')        

    @property
    def shortInterest(self) -> float:
        """Short interest value."""
        return self.__shortInterest

    @shortInterest.setter
    def shortInterest(self, value: float):
        self.__shortInterest = value
        self._property_changed('shortInterest')        

    @property
    def referencePeriod(self) -> str:
        """The period for which released data refers to."""
        return self.__referencePeriod

    @referencePeriod.setter
    def referencePeriod(self, value: str):
        self.__referencePeriod = value
        self._property_changed('referencePeriod')        

    @property
    def adjustedVolume(self) -> float:
        """Accumulated number of shares, lots or contracts traded according to the market convention adjusted for corporate actions."""
        return self.__adjustedVolume

    @adjustedVolume.setter
    def adjustedVolume(self, value: float):
        self.__adjustedVolume = value
        self._property_changed('adjustedVolume')        

    @property
    def restrictionEndDate(self) -> datetime.date:
        """The date at which the security restriction was lifted."""
        return self.__restrictionEndDate

    @restrictionEndDate.setter
    def restrictionEndDate(self, value: datetime.date):
        self.__restrictionEndDate = value
        self._property_changed('restrictionEndDate')        

    @property
    def queueInLotsDescription(self) -> str:
        """Description of the Stock's Queue size in Lots (if applicable) on the particular date."""
        return self.__queueInLotsDescription

    @queueInLotsDescription.setter
    def queueInLotsDescription(self, value: str):
        self.__queueInLotsDescription = value
        self._property_changed('queueInLotsDescription')        

    @property
    def pbClientId(self) -> str:
        """Prime Brokerage client identifier."""
        return self.__pbClientId

    @pbClientId.setter
    def pbClientId(self, value: str):
        self.__pbClientId = value
        self._property_changed('pbClientId')        

    @property
    def ownerId(self) -> str:
        """Marquee unique identifier for user who owns the object."""
        return self.__ownerId

    @ownerId.setter
    def ownerId(self, value: str):
        self.__ownerId = value
        self._property_changed('ownerId')        

    @property
    def secDB(self) -> str:
        """Internal Goldman Sachs security database location for the asset."""
        return self.__secDB

    @secDB.setter
    def secDB(self, value: str):
        self.__secDB = value
        self._property_changed('secDB')        

    @property
    def composite10DayAdv(self) -> float:
        """Composite 10 day ADV."""
        return self.__composite10DayAdv

    @composite10DayAdv.setter
    def composite10DayAdv(self, value: float):
        self.__composite10DayAdv = value
        self._property_changed('composite10DayAdv')        

    @property
    def objective(self) -> str:
        """The objective of the hedge."""
        return self.__objective

    @objective.setter
    def objective(self, value: str):
        self.__objective = value
        self._property_changed('objective')        

    @property
    def bpeQualityStars(self) -> float:
        """Confidence in the BPE."""
        return self.__bpeQualityStars

    @bpeQualityStars.setter
    def bpeQualityStars(self, value: float):
        self.__bpeQualityStars = value
        self._property_changed('bpeQualityStars')        

    @property
    def navPrice(self) -> float:
        """Net asset value price. Quoted price (mid, 100 ??? Upfront) of the underlying basket of single name CDS. (Theoretical Index value). In percent."""
        return self.__navPrice

    @navPrice.setter
    def navPrice(self, value: float):
        self.__navPrice = value
        self._property_changed('navPrice')        

    @property
    def ideaActivityType(self) -> str:
        """Equals CorporateAction if the activity originates as a result of a corporate action. Equals GovernanceAction if the activity originates as a result of a control measure. Equals UserAction if the activity is user driven."""
        return self.__ideaActivityType

    @ideaActivityType.setter
    def ideaActivityType(self, value: str):
        self.__ideaActivityType = value
        self._property_changed('ideaActivityType')        

    @property
    def precipitation(self) -> float:
        """Amount of rainfall in inches."""
        return self.__precipitation

    @precipitation.setter
    def precipitation(self, value: float):
        self.__precipitation = value
        self._property_changed('precipitation')        

    @property
    def ideaSource(self) -> str:
        """Equals User if the idea activity originates from a sales person. Equals System if the idea activity is system generated."""
        return self.__ideaSource

    @ideaSource.setter
    def ideaSource(self, value: str):
        self.__ideaSource = value
        self._property_changed('ideaSource')        

    @property
    def hedgeNotional(self) -> float:
        """Notional value of the hedge."""
        return self.__hedgeNotional

    @hedgeNotional.setter
    def hedgeNotional(self, value: float):
        self.__hedgeNotional = value
        self._property_changed('hedgeNotional')        

    @property
    def askLow(self) -> float:
        """The lowest ask Price (price offering to sell)."""
        return self.__askLow

    @askLow.setter
    def askLow(self, value: float):
        self.__askLow = value
        self._property_changed('askLow')        

    @property
    def unadjustedAsk(self) -> float:
        """Unadjusted ask level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__unadjustedAsk

    @unadjustedAsk.setter
    def unadjustedAsk(self, value: float):
        self.__unadjustedAsk = value
        self._property_changed('unadjustedAsk')        

    @property
    def betaAdjustedNetExposure(self) -> float:
        """Beta adjusted net exposure."""
        return self.__betaAdjustedNetExposure

    @betaAdjustedNetExposure.setter
    def betaAdjustedNetExposure(self, value: float):
        self.__betaAdjustedNetExposure = value
        self._property_changed('betaAdjustedNetExposure')        

    @property
    def expiry(self) -> str:
        """The time period before the option expires."""
        return self.__expiry

    @expiry.setter
    def expiry(self, value: str):
        self.__expiry = value
        self._property_changed('expiry')        

    @property
    def tradingPnl(self) -> float:
        """Trading Profit and Loss (PNL)."""
        return self.__tradingPnl

    @tradingPnl.setter
    def tradingPnl(self, value: float):
        self.__tradingPnl = value
        self._property_changed('tradingPnl')        

    @property
    def strikePercentage(self) -> float:
        """Strike compared to market value."""
        return self.__strikePercentage

    @strikePercentage.setter
    def strikePercentage(self, value: float):
        self.__strikePercentage = value
        self._property_changed('strikePercentage')        

    @property
    def excessReturnPrice(self) -> float:
        """The excess return price of an instrument."""
        return self.__excessReturnPrice

    @excessReturnPrice.setter
    def excessReturnPrice(self, value: float):
        self.__excessReturnPrice = value
        self._property_changed('excessReturnPrice')        

    @property
    def givenPlusPaid(self) -> float:
        """Total of given & paid."""
        return self.__givenPlusPaid

    @givenPlusPaid.setter
    def givenPlusPaid(self, value: float):
        self.__givenPlusPaid = value
        self._property_changed('givenPlusPaid')        

    @property
    def shortConvictionSmall(self) -> float:
        """The count of short ideas with small conviction."""
        return self.__shortConvictionSmall

    @shortConvictionSmall.setter
    def shortConvictionSmall(self, value: float):
        self.__shortConvictionSmall = value
        self._property_changed('shortConvictionSmall')        

    @property
    def prevCloseBid(self) -> float:
        """Previous close BID price."""
        return self.__prevCloseBid

    @prevCloseBid.setter
    def prevCloseBid(self, value: float):
        self.__prevCloseBid = value
        self._property_changed('prevCloseBid')        

    @property
    def fxPnl(self) -> float:
        """Foreign Exchange Profit and Loss (PNL)."""
        return self.__fxPnl

    @fxPnl.setter
    def fxPnl(self, value: float):
        self.__fxPnl = value
        self._property_changed('fxPnl')        

    @property
    def forecast(self) -> float:
        """Forward FX forecast."""
        return self.__forecast

    @forecast.setter
    def forecast(self, value: float):
        self.__forecast = value
        self._property_changed('forecast')        

    @property
    def tcmCostHorizon16Day(self) -> float:
        """TCM cost with a 16 day time horizon."""
        return self.__tcmCostHorizon16Day

    @tcmCostHorizon16Day.setter
    def tcmCostHorizon16Day(self, value: float):
        self.__tcmCostHorizon16Day = value
        self._property_changed('tcmCostHorizon16Day')        

    @property
    def pnl(self) -> float:
        """Profit and Loss."""
        return self.__pnl

    @pnl.setter
    def pnl(self, value: float):
        self.__pnl = value
        self._property_changed('pnl')        

    @property
    def assetClassificationsGicsIndustryGroup(self) -> str:
        """GICS Industry Group classification (level 2)."""
        return self.__assetClassificationsGicsIndustryGroup

    @assetClassificationsGicsIndustryGroup.setter
    def assetClassificationsGicsIndustryGroup(self, value: str):
        self.__assetClassificationsGicsIndustryGroup = value
        self._property_changed('assetClassificationsGicsIndustryGroup')        

    @property
    def unadjustedClose(self) -> float:
        """Unadjusted Close level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__unadjustedClose

    @unadjustedClose.setter
    def unadjustedClose(self, value: float):
        self.__unadjustedClose = value
        self._property_changed('unadjustedClose')        

    @property
    def tcmCostHorizon4Day(self) -> float:
        """TCM cost with a 4 day time horizon."""
        return self.__tcmCostHorizon4Day

    @tcmCostHorizon4Day.setter
    def tcmCostHorizon4Day(self, value: float):
        self.__tcmCostHorizon4Day = value
        self._property_changed('tcmCostHorizon4Day')        

    @property
    def assetClassificationsIsPrimary(self) -> bool:
        """Whether or not it is the primary exchange asset."""
        return self.__assetClassificationsIsPrimary

    @assetClassificationsIsPrimary.setter
    def assetClassificationsIsPrimary(self, value: bool):
        self.__assetClassificationsIsPrimary = value
        self._property_changed('assetClassificationsIsPrimary')        

    @property
    def loanDate(self) -> datetime.date:
        """The date at which the securities loan was enacted."""
        return self.__loanDate

    @loanDate.setter
    def loanDate(self, value: datetime.date):
        self.__loanDate = value
        self._property_changed('loanDate')        

    @property
    def styles(self) -> Tuple[Tuple[str, ...], ...]:
        """Styles or themes associated with the asset (max 50)"""
        return self.__styles

    @styles.setter
    def styles(self, value: Tuple[Tuple[str, ...], ...]):
        self.__styles = value
        self._property_changed('styles')        

    @property
    def lendingSecId(self) -> str:
        """Securities lending identifiter for the security on loan."""
        return self.__lendingSecId

    @lendingSecId.setter
    def lendingSecId(self, value: str):
        self.__lendingSecId = value
        self._property_changed('lendingSecId')        

    @property
    def shortName(self) -> str:
        """Short name."""
        return self.__shortName

    @shortName.setter
    def shortName(self, value: str):
        self.__shortName = value
        self._property_changed('shortName')        

    @property
    def equityTheta(self) -> float:
        """Theta exposure to equity products."""
        return self.__equityTheta

    @equityTheta.setter
    def equityTheta(self, value: float):
        self.__equityTheta = value
        self._property_changed('equityTheta')        

    @property
    def averageFillPrice(self) -> float:
        """Average fill price for the order since it started."""
        return self.__averageFillPrice

    @averageFillPrice.setter
    def averageFillPrice(self, value: float):
        self.__averageFillPrice = value
        self._property_changed('averageFillPrice')        

    @property
    def snowfall(self) -> float:
        """Amount of snowfall in inches."""
        return self.__snowfall

    @snowfall.setter
    def snowfall(self, value: float):
        self.__snowfall = value
        self._property_changed('snowfall')        

    @property
    def mic(self) -> str:
        """Market identifier code."""
        return self.__mic

    @mic.setter
    def mic(self, value: str):
        self.__mic = value
        self._property_changed('mic')        

    @property
    def bidGspread(self) -> float:
        """Bid G spread."""
        return self.__bidGspread

    @bidGspread.setter
    def bidGspread(self, value: float):
        self.__bidGspread = value
        self._property_changed('bidGspread')        

    @property
    def openPrice(self) -> float:
        """Opening level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__openPrice

    @openPrice.setter
    def openPrice(self, value: float):
        self.__openPrice = value
        self._property_changed('openPrice')        

    @property
    def mid(self) -> float:
        """Mid."""
        return self.__mid

    @mid.setter
    def mid(self, value: float):
        self.__mid = value
        self._property_changed('mid')        

    @property
    def autoExecState(self) -> str:
        """Auto Execution State."""
        return self.__autoExecState

    @autoExecState.setter
    def autoExecState(self, value: str):
        self.__autoExecState = value
        self._property_changed('autoExecState')        

    @property
    def depthSpreadScore(self) -> float:
        """Z-score of the difference between the mid price and the best price an order to buy or sell a specific notional can be filled at."""
        return self.__depthSpreadScore

    @depthSpreadScore.setter
    def depthSpreadScore(self, value: float):
        self.__depthSpreadScore = value
        self._property_changed('depthSpreadScore')        

    @property
    def relativeReturnYtd(self) -> float:
        """Relative Return Year to Date."""
        return self.__relativeReturnYtd

    @relativeReturnYtd.setter
    def relativeReturnYtd(self, value: float):
        self.__relativeReturnYtd = value
        self._property_changed('relativeReturnYtd')        

    @property
    def long(self) -> float:
        """Long exposure."""
        return self.__long

    @long.setter
    def long(self, value: float):
        self.__long = value
        self._property_changed('long')        

    @property
    def subAccount(self) -> str:
        """Subaccount."""
        return self.__subAccount

    @subAccount.setter
    def subAccount(self, value: str):
        self.__subAccount = value
        self._property_changed('subAccount')        

    @property
    def fairVolatility(self) -> float:
        """Strike in volatility terms, calculated as square root of fair variance."""
        return self.__fairVolatility

    @fairVolatility.setter
    def fairVolatility(self, value: float):
        self.__fairVolatility = value
        self._property_changed('fairVolatility')        

    @property
    def dollarCross(self) -> str:
        """USD cross symbol for a particular currency."""
        return self.__dollarCross

    @dollarCross.setter
    def dollarCross(self, value: str):
        self.__dollarCross = value
        self._property_changed('dollarCross')        

    @property
    def portfolioType(self) -> str:
        """Portfolio type differentiates the portfolio categorization"""
        return self.__portfolioType

    @portfolioType.setter
    def portfolioType(self, value: str):
        self.__portfolioType = value
        self._property_changed('portfolioType')        

    @property
    def longWeight(self) -> float:
        """Long weight of a position in a given portfolio. Equivalent to position long exposure / total long exposure. If you have a position with a longExposure of $20, and your portfolio longExposure is $100, longWeight would be 0.2 (20/100)."""
        return self.__longWeight

    @longWeight.setter
    def longWeight(self, value: float):
        self.__longWeight = value
        self._property_changed('longWeight')        

    @property
    def calculationTime(self) -> int:
        """Time taken to calculate risk metric (ms)."""
        return self.__calculationTime

    @calculationTime.setter
    def calculationTime(self, value: int):
        self.__calculationTime = value
        self._property_changed('calculationTime')        

    @property
    def vendor(self) -> str:
        """Vendor of dataset."""
        return self.__vendor

    @vendor.setter
    def vendor(self, value: str):
        self.__vendor = value
        self._property_changed('vendor')        

    @property
    def currency(self) -> str:
        """Currency, ISO 4217 currency code or exchange quote modifier (e.g. GBP vs GBp)"""
        return self.__currency

    @currency.setter
    def currency(self, value: str):
        self.__currency = value
        self._property_changed('currency')        

    @property
    def realTimeRestrictionStatus(self) -> Tuple[Tuple[str, ...], ...]:
        """Real Time Restricted status as set by compliance."""
        return self.__realTimeRestrictionStatus

    @realTimeRestrictionStatus.setter
    def realTimeRestrictionStatus(self, value: Tuple[Tuple[str, ...], ...]):
        self.__realTimeRestrictionStatus = value
        self._property_changed('realTimeRestrictionStatus')        

    @property
    def averageRealizedVariance(self) -> float:
        """Average variance of an asset realized by observations of market prices."""
        return self.__averageRealizedVariance

    @averageRealizedVariance.setter
    def averageRealizedVariance(self, value: float):
        self.__averageRealizedVariance = value
        self._property_changed('averageRealizedVariance')        

    @property
    def clusterClass(self) -> str:
        """The Cluster the stock belongs on the particular date. The cluster class will be assigned to a value between 1 and 13 (inclusive)."""
        return self.__clusterClass

    @clusterClass.setter
    def clusterClass(self, value: str):
        self.__clusterClass = value
        self._property_changed('clusterClass')        

    @property
    def financialReturnsScore(self) -> float:
        """Financial Returns percentile relative to Americas coverage universe (a higher score means stronger financial returns)."""
        return self.__financialReturnsScore

    @financialReturnsScore.setter
    def financialReturnsScore(self, value: float):
        self.__financialReturnsScore = value
        self._property_changed('financialReturnsScore')        

    @property
    def netChange(self) -> float:
        """Difference between the lastest trading price or value and the adjusted historical closing value or settlement price."""
        return self.__netChange

    @netChange.setter
    def netChange(self, value: float):
        self.__netChange = value
        self._property_changed('netChange')        

    @property
    def nonSymbolDimensions(self) -> Tuple[str, ...]:
        """Fields that are not nullable."""
        return self.__nonSymbolDimensions

    @nonSymbolDimensions.setter
    def nonSymbolDimensions(self, value: Tuple[str, ...]):
        self.__nonSymbolDimensions = value
        self._property_changed('nonSymbolDimensions')        

    @property
    def queueingTime(self) -> int:
        """Time for which risk calculation was queued (ms)."""
        return self.__queueingTime

    @queueingTime.setter
    def queueingTime(self, value: int):
        self.__queueingTime = value
        self._property_changed('queueingTime')        

    @property
    def bidSize(self) -> float:
        """The number of shares, lots, or contracts willing to buy at the Bid price."""
        return self.__bidSize

    @bidSize.setter
    def bidSize(self, value: float):
        self.__bidSize = value
        self._property_changed('bidSize')        

    @property
    def swapType(self) -> str:
        """Swap type of position."""
        return self.__swapType

    @swapType.setter
    def swapType(self, value: str):
        self.__swapType = value
        self._property_changed('swapType')        

    @property
    def arrivalMid(self) -> float:
        """Arrival Mid Price."""
        return self.__arrivalMid

    @arrivalMid.setter
    def arrivalMid(self, value: float):
        self.__arrivalMid = value
        self._property_changed('arrivalMid')        

    @property
    def sellSettleDate(self) -> datetime.date:
        """Data that the sell of securities will settle."""
        return self.__sellSettleDate

    @sellSettleDate.setter
    def sellSettleDate(self, value: datetime.date):
        self.__sellSettleDate = value
        self._property_changed('sellSettleDate')        

    @property
    def assetParametersExchangeCurrency(self) -> str:
        """Currency, ISO 4217 currency code or exchange quote modifier (e.g. GBP vs GBp)"""
        return self.__assetParametersExchangeCurrency

    @assetParametersExchangeCurrency.setter
    def assetParametersExchangeCurrency(self, value: str):
        self.__assetParametersExchangeCurrency = value
        self._property_changed('assetParametersExchangeCurrency')        

    @property
    def unexplained(self) -> float:
        """PNL unexplained by risk model."""
        return self.__unexplained

    @unexplained.setter
    def unexplained(self, value: float):
        self.__unexplained = value
        self._property_changed('unexplained')        

    @property
    def assetClassificationsCountryName(self) -> str:
        """Country name of asset."""
        return self.__assetClassificationsCountryName

    @assetClassificationsCountryName.setter
    def assetClassificationsCountryName(self, value: str):
        self.__assetClassificationsCountryName = value
        self._property_changed('assetClassificationsCountryName')        

    @property
    def metric(self) -> str:
        """Metric for the associated asset."""
        return self.__metric

    @metric.setter
    def metric(self, value: str):
        self.__metric = value
        self._property_changed('metric')        

    @property
    def newIdeasYtd(self) -> float:
        """Ideas received by clients Year to date."""
        return self.__newIdeasYtd

    @newIdeasYtd.setter
    def newIdeasYtd(self, value: float):
        self.__newIdeasYtd = value
        self._property_changed('newIdeasYtd')        

    @property
    def managementFee(self) -> Union[float, Op]:
        return self.__managementFee

    @managementFee.setter
    def managementFee(self, value: Union[float, Op]):
        self.__managementFee = value
        self._property_changed('managementFee')        

    @property
    def ask(self) -> float:
        """Latest Ask Price (price offering to sell)."""
        return self.__ask

    @ask.setter
    def ask(self, value: float):
        self.__ask = value
        self._property_changed('ask')        

    @property
    def impliedLognormalVolatility(self) -> float:
        """Market implied volatility measured using a lognormal model in percent/year."""
        return self.__impliedLognormalVolatility

    @impliedLognormalVolatility.setter
    def impliedLognormalVolatility(self, value: float):
        self.__impliedLognormalVolatility = value
        self._property_changed('impliedLognormalVolatility')        

    @property
    def closePrice(self) -> float:
        """Closing level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__closePrice

    @closePrice.setter
    def closePrice(self, value: float):
        self.__closePrice = value
        self._property_changed('closePrice')        

    @property
    def endTime(self) -> datetime.datetime:
        """End time."""
        return self.__endTime

    @endTime.setter
    def endTime(self, value: datetime.datetime):
        self.__endTime = value
        self._property_changed('endTime')        

    @property
    def open(self) -> float:
        """Opening level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__open

    @open.setter
    def open(self, value: float):
        self.__open = value
        self._property_changed('open')        

    @property
    def sourceId(self) -> str:
        """Unique id of data provider."""
        return self.__sourceId

    @sourceId.setter
    def sourceId(self, value: str):
        self.__sourceId = value
        self._property_changed('sourceId')        

    @property
    def country(self) -> str:
        """Country of incorporation of asset."""
        return self.__country

    @country.setter
    def country(self, value: str):
        self.__country = value
        self._property_changed('country')        

    @property
    def cusip(self) -> str:
        """CUSIP - Committee on Uniform Securities Identification Procedures number (subject to licensing)."""
        return self.__cusip

    @cusip.setter
    def cusip(self, value: str):
        self.__cusip = value
        self._property_changed('cusip')        

    @property
    def ideaActivityTime(self) -> datetime.datetime:
        """The time the idea activity took place. If ideaStatus is open, the time reflects the Idea creation time. If ideaStatus is closed, the time reflects the time the idea was closed."""
        return self.__ideaActivityTime

    @ideaActivityTime.setter
    def ideaActivityTime(self, value: datetime.datetime):
        self.__ideaActivityTime = value
        self._property_changed('ideaActivityTime')        

    @property
    def touchSpreadScore(self) -> float:
        """Z-score of the difference between highest bid and lowest offer."""
        return self.__touchSpreadScore

    @touchSpreadScore.setter
    def touchSpreadScore(self, value: float):
        self.__touchSpreadScore = value
        self._property_changed('touchSpreadScore')        

    @property
    def absoluteStrike(self) -> float:
        """Spot * relative strike in local currency."""
        return self.__absoluteStrike

    @absoluteStrike.setter
    def absoluteStrike(self, value: float):
        self.__absoluteStrike = value
        self._property_changed('absoluteStrike')        

    @property
    def netExposure(self) -> float:
        """The difference between long and short exposure in the portfolio. If you are $60 short and $40 long, then the netExposure would be -$20 (-60+40)."""
        return self.__netExposure

    @netExposure.setter
    def netExposure(self, value: float):
        self.__netExposure = value
        self._property_changed('netExposure')        

    @property
    def source(self) -> str:
        """Source of data."""
        return self.__source

    @source.setter
    def source(self, value: str):
        self.__source = value
        self._property_changed('source')        

    @property
    def assetClassificationsCountryCode(self) -> str:
        """Country code (ISO 3166)."""
        return self.__assetClassificationsCountryCode

    @assetClassificationsCountryCode.setter
    def assetClassificationsCountryCode(self, value: str):
        self.__assetClassificationsCountryCode = value
        self._property_changed('assetClassificationsCountryCode')        

    @property
    def frequency(self) -> str:
        """Requested frequency of data delivery."""
        return self.__frequency

    @frequency.setter
    def frequency(self, value: str):
        self.__frequency = value
        self._property_changed('frequency')        

    @property
    def activityId(self) -> str:
        """Marquee unique Activity identifier."""
        return self.__activityId

    @activityId.setter
    def activityId(self, value: str):
        self.__activityId = value
        self._property_changed('activityId')        

    @property
    def estimatedImpact(self) -> float:
        """Likely impact of a proposed trade on the price of an asset (bps). The model's shortfall estimates reflect how much it cost to execute similar trades in the past, as opposed to providing a hypothetical cost derived using tick data."""
        return self.__estimatedImpact

    @estimatedImpact.setter
    def estimatedImpact(self, value: float):
        self.__estimatedImpact = value
        self._property_changed('estimatedImpact')        

    @property
    def dataSetSubCategory(self) -> str:
        """Second level grouping of dataset."""
        return self.__dataSetSubCategory

    @dataSetSubCategory.setter
    def dataSetSubCategory(self, value: str):
        self.__dataSetSubCategory = value
        self._property_changed('dataSetSubCategory')        

    @property
    def loanSpreadBucket(self) -> str:
        """The difference between the investment rate on cash collateral and the rebate rate of a loan."""
        return self.__loanSpreadBucket

    @loanSpreadBucket.setter
    def loanSpreadBucket(self, value: str):
        self.__loanSpreadBucket = value
        self._property_changed('loanSpreadBucket')        

    @property
    def assetParametersPricingLocation(self) -> str:
        """The location in which the asset was priced."""
        return self.__assetParametersPricingLocation

    @assetParametersPricingLocation.setter
    def assetParametersPricingLocation(self, value: str):
        self.__assetParametersPricingLocation = value
        self._property_changed('assetParametersPricingLocation')        

    @property
    def eventDescription(self) -> str:
        """Short description of the event, providing additional information beyond eventType."""
        return self.__eventDescription

    @eventDescription.setter
    def eventDescription(self, value: str):
        self.__eventDescription = value
        self._property_changed('eventDescription')        

    @property
    def strikeReference(self) -> str:
        """Reference for strike level (enum: spot, forward)."""
        return self.__strikeReference

    @strikeReference.setter
    def strikeReference(self, value: str):
        self.__strikeReference = value
        self._property_changed('strikeReference')        

    @property
    def details(self) -> str:
        """Corporate action details."""
        return self.__details

    @details.setter
    def details(self, value: str):
        self.__details = value
        self._property_changed('details')        

    @property
    def assetCount(self) -> float:
        """Number of assets in a portfolio or index."""
        return self.__assetCount

    @assetCount.setter
    def assetCount(self, value: float):
        self.__assetCount = value
        self._property_changed('assetCount')        

    @property
    def quantityBucket(self) -> str:
        """Range of pricing hours."""
        return self.__quantityBucket

    @quantityBucket.setter
    def quantityBucket(self, value: str):
        self.__quantityBucket = value
        self._property_changed('quantityBucket')        

    @property
    def oeName(self) -> str:
        """Name of user's organization."""
        return self.__oeName

    @oeName.setter
    def oeName(self, value: str):
        self.__oeName = value
        self._property_changed('oeName')        

    @property
    def given(self) -> float:
        """Number of trades given."""
        return self.__given

    @given.setter
    def given(self, value: float):
        self.__given = value
        self._property_changed('given')        

    @property
    def absoluteValue(self) -> float:
        """The notional value of the asset."""
        return self.__absoluteValue

    @absoluteValue.setter
    def absoluteValue(self, value: float):
        self.__absoluteValue = value
        self._property_changed('absoluteValue')        

    @property
    def delistingDate(self) -> str:
        """Date at which the entity is delisted."""
        return self.__delistingDate

    @delistingDate.setter
    def delistingDate(self, value: str):
        self.__delistingDate = value
        self._property_changed('delistingDate')        

    @property
    def longTenor(self) -> str:
        """Tenor of instrument."""
        return self.__longTenor

    @longTenor.setter
    def longTenor(self, value: str):
        self.__longTenor = value
        self._property_changed('longTenor')        

    @property
    def mctr(self) -> float:
        """Marginal contribution of a given asset to portfolio variance, is dependent on covariance matrix."""
        return self.__mctr

    @mctr.setter
    def mctr(self, value: float):
        self.__mctr = value
        self._property_changed('mctr')        

    @property
    def weight(self) -> float:
        """Weight of a given position within a portfolio, by default calcualted as netWeight."""
        return self.__weight

    @weight.setter
    def weight(self, value: float):
        self.__weight = value
        self._property_changed('weight')        

    @property
    def historicalClose(self) -> float:
        """Historical Close Price."""
        return self.__historicalClose

    @historicalClose.setter
    def historicalClose(self, value: float):
        self.__historicalClose = value
        self._property_changed('historicalClose')        

    @property
    def assetCountPriced(self) -> float:
        """Number of assets in a portfolio which could be priced."""
        return self.__assetCountPriced

    @assetCountPriced.setter
    def assetCountPriced(self, value: float):
        self.__assetCountPriced = value
        self._property_changed('assetCountPriced')        

    @property
    def marketDataPoint(self) -> Tuple[Tuple[str, ...], ...]:
        """The market data point (e.g. 3m, 10y, 11y, Dec19)."""
        return self.__marketDataPoint

    @marketDataPoint.setter
    def marketDataPoint(self, value: Tuple[Tuple[str, ...], ...]):
        self.__marketDataPoint = value
        self._property_changed('marketDataPoint')        

    @property
    def ideaId(self) -> str:
        """Marquee unique asset identifier."""
        return self.__ideaId

    @ideaId.setter
    def ideaId(self, value: str):
        self.__ideaId = value
        self._property_changed('ideaId')        

    @property
    def commentStatus(self) -> str:
        """Corporate action comment status."""
        return self.__commentStatus

    @commentStatus.setter
    def commentStatus(self, value: str):
        self.__commentStatus = value
        self._property_changed('commentStatus')        

    @property
    def marginalCost(self) -> float:
        """Marginal cost."""
        return self.__marginalCost

    @marginalCost.setter
    def marginalCost(self, value: float):
        self.__marginalCost = value
        self._property_changed('marginalCost')        

    @property
    def absoluteWeight(self) -> float:
        """Weight in terms of absolute notional."""
        return self.__absoluteWeight

    @absoluteWeight.setter
    def absoluteWeight(self, value: float):
        self.__absoluteWeight = value
        self._property_changed('absoluteWeight')        

    @property
    def tradeTime(self) -> datetime.datetime:
        """Trade Time."""
        return self.__tradeTime

    @tradeTime.setter
    def tradeTime(self, value: datetime.datetime):
        self.__tradeTime = value
        self._property_changed('tradeTime')        

    @property
    def measure(self) -> str:
        """A calculated metric in the risk scenario."""
        return self.__measure

    @measure.setter
    def measure(self, value: str):
        self.__measure = value
        self._property_changed('measure')        

    @property
    def clientWeight(self) -> float:
        """Weight of client positions in the region or sector (%)."""
        return self.__clientWeight

    @clientWeight.setter
    def clientWeight(self, value: float):
        self.__clientWeight = value
        self._property_changed('clientWeight')        

    @property
    def hedgeAnnualizedVolatility(self) -> float:
        """Standard deviation of the annualized returns."""
        return self.__hedgeAnnualizedVolatility

    @hedgeAnnualizedVolatility.setter
    def hedgeAnnualizedVolatility(self, value: float):
        self.__hedgeAnnualizedVolatility = value
        self._property_changed('hedgeAnnualizedVolatility')        

    @property
    def benchmarkCurrency(self) -> str:
        """Currency, ISO 4217 currency code or exchange quote modifier (e.g. GBP vs GBp)"""
        return self.__benchmarkCurrency

    @benchmarkCurrency.setter
    def benchmarkCurrency(self, value: str):
        self.__benchmarkCurrency = value
        self._property_changed('benchmarkCurrency')        

    @property
    def name(self) -> str:
        """Legal or published name for the asset."""
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value
        self._property_changed('name')        

    @property
    def aum(self) -> Union[float, Op]:
        return self.__aum

    @aum.setter
    def aum(self, value: Union[float, Op]):
        self.__aum = value
        self._property_changed('aum')        

    @property
    def folderName(self) -> str:
        """Folder Name of a chart."""
        return self.__folderName

    @folderName.setter
    def folderName(self, value: str):
        self.__folderName = value
        self._property_changed('folderName')        

    @property
    def lendingPartnerFee(self) -> float:
        """Fee earned by the Lending Partner in a securities lending agreement."""
        return self.__lendingPartnerFee

    @lendingPartnerFee.setter
    def lendingPartnerFee(self, value: float):
        self.__lendingPartnerFee = value
        self._property_changed('lendingPartnerFee')        

    @property
    def region(self) -> str:
        """Regional classification for the asset"""
        return self.__region

    @region.setter
    def region(self, value: str):
        self.__region = value
        self._property_changed('region')        

    @property
    def liveDate(self) -> Union[datetime.date, Op]:
        return self.__liveDate

    @liveDate.setter
    def liveDate(self, value: Union[datetime.date, Op]):
        self.__liveDate = value
        self._property_changed('liveDate')        

    @property
    def askHigh(self) -> float:
        """The highest Ask Price (price offering to sell)."""
        return self.__askHigh

    @askHigh.setter
    def askHigh(self, value: float):
        self.__askHigh = value
        self._property_changed('askHigh')        

    @property
    def corporateActionType(self) -> str:
        """Different types of corporate actions from solactive"""
        return self.__corporateActionType

    @corporateActionType.setter
    def corporateActionType(self, value: str):
        self.__corporateActionType = value
        self._property_changed('corporateActionType')        

    @property
    def primeId(self) -> str:
        """Prime Id."""
        return self.__primeId

    @primeId.setter
    def primeId(self, value: str):
        self.__primeId = value
        self._property_changed('primeId')        

    @property
    def tenor2(self) -> str:
        """Tenor of instrument."""
        return self.__tenor2

    @tenor2.setter
    def tenor2(self, value: str):
        self.__tenor2 = value
        self._property_changed('tenor2')        

    @property
    def description(self) -> str:
        """Description of asset."""
        return self.__description

    @description.setter
    def description(self, value: str):
        self.__description = value
        self._property_changed('description')        

    @property
    def valueRevised(self) -> str:
        """Revised value."""
        return self.__valueRevised

    @valueRevised.setter
    def valueRevised(self, value: str):
        self.__valueRevised = value
        self._property_changed('valueRevised')        

    @property
    def ownerName(self) -> str:
        """Name of person submitting request."""
        return self.__ownerName

    @ownerName.setter
    def ownerName(self, value: str):
        self.__ownerName = value
        self._property_changed('ownerName')        

    @property
    def adjustedTradePrice(self) -> float:
        """Last trade price or value adjusted for corporate actions."""
        return self.__adjustedTradePrice

    @adjustedTradePrice.setter
    def adjustedTradePrice(self, value: float):
        self.__adjustedTradePrice = value
        self._property_changed('adjustedTradePrice')        

    @property
    def lastUpdatedById(self) -> str:
        """Unique identifier of user who last updated the object"""
        return self.__lastUpdatedById

    @lastUpdatedById.setter
    def lastUpdatedById(self, value: str):
        self.__lastUpdatedById = value
        self._property_changed('lastUpdatedById')        

    @property
    def zScore(self) -> float:
        """Z Score."""
        return self.__zScore

    @zScore.setter
    def zScore(self, value: float):
        self.__zScore = value
        self._property_changed('zScore')        

    @property
    def targetShareholderMeetingDate(self) -> str:
        """Target acquisition entity shareholder meeting date."""
        return self.__targetShareholderMeetingDate

    @targetShareholderMeetingDate.setter
    def targetShareholderMeetingDate(self, value: str):
        self.__targetShareholderMeetingDate = value
        self._property_changed('targetShareholderMeetingDate')        

    @property
    def collateralMarketValue(self) -> float:
        """Marketable value of a given collateral position, generally the market price for a given date."""
        return self.__collateralMarketValue

    @collateralMarketValue.setter
    def collateralMarketValue(self, value: float):
        self.__collateralMarketValue = value
        self._property_changed('collateralMarketValue')        

    @property
    def isADR(self) -> bool:
        """Is ADR or not."""
        return self.__isADR

    @isADR.setter
    def isADR(self, value: bool):
        self.__isADR = value
        self._property_changed('isADR')        

    @property
    def eventStartTime(self) -> str:
        """The start time of the event if the event occurs during a time window and the event has a specific start time. It is represented in HH:MM 24 hour format in the time zone of the exchange where the company is listed."""
        return self.__eventStartTime

    @eventStartTime.setter
    def eventStartTime(self, value: str):
        self.__eventStartTime = value
        self._property_changed('eventStartTime')        

    @property
    def factor(self) -> str:
        """For Axioma, one of: Exchange Rate Sensitivity, Growth, Leverage, Medium-Term Momentum, Short-Term Momentum, Size, Value, Volatility. For Prime, one of: Long Concentration, Short Concentration, Long Crowdedness, Short Crowdedness, Crowdedness momentum, Short Conviction."""
        return self.__factor

    @factor.setter
    def factor(self, value: str):
        self.__factor = value
        self._property_changed('factor')        

    @property
    def daysOnLoan(self) -> float:
        """The number of days this loan as been on our books."""
        return self.__daysOnLoan

    @daysOnLoan.setter
    def daysOnLoan(self, value: float):
        self.__daysOnLoan = value
        self._property_changed('daysOnLoan')        

    @property
    def longConvictionSmall(self) -> float:
        """The count of long ideas with small conviction."""
        return self.__longConvictionSmall

    @longConvictionSmall.setter
    def longConvictionSmall(self, value: float):
        self.__longConvictionSmall = value
        self._property_changed('longConvictionSmall')        

    @property
    def serviceId(self) -> str:
        """Service ID."""
        return self.__serviceId

    @serviceId.setter
    def serviceId(self, value: str):
        self.__serviceId = value
        self._property_changed('serviceId')        

    @property
    def turnover(self) -> float:
        """Turnover."""
        return self.__turnover

    @turnover.setter
    def turnover(self, value: float):
        self.__turnover = value
        self._property_changed('turnover')        

    @property
    def complianceEffectiveTime(self) -> datetime.datetime:
        """Time that the compliance status became effective."""
        return self.__complianceEffectiveTime

    @complianceEffectiveTime.setter
    def complianceEffectiveTime(self, value: datetime.datetime):
        self.__complianceEffectiveTime = value
        self._property_changed('complianceEffectiveTime')        

    @property
    def expirationDate(self) -> datetime.date:
        """The expiration date of the associated contract and the last date it trades."""
        return self.__expirationDate

    @expirationDate.setter
    def expirationDate(self, value: datetime.date):
        self.__expirationDate = value
        self._property_changed('expirationDate')        

    @property
    def gsfeer(self) -> float:
        """Goldman Sachs Fundamental Equilibrium Exchange Rate."""
        return self.__gsfeer

    @gsfeer.setter
    def gsfeer(self, value: float):
        self.__gsfeer = value
        self._property_changed('gsfeer')        

    @property
    def coverage(self) -> str:
        """Coverage of dataset."""
        return self.__coverage

    @coverage.setter
    def coverage(self, value: str):
        self.__coverage = value
        self._property_changed('coverage')        

    @property
    def backtestId(self) -> str:
        """Marquee unique backtest identifier."""
        return self.__backtestId

    @backtestId.setter
    def backtestId(self, value: str):
        self.__backtestId = value
        self._property_changed('backtestId')        

    @property
    def gPercentile(self) -> float:
        """Percentile based on G score."""
        return self.__gPercentile

    @gPercentile.setter
    def gPercentile(self, value: float):
        self.__gPercentile = value
        self._property_changed('gPercentile')        

    @property
    def gScore(self) -> float:
        """Score for governance metrics."""
        return self.__gScore

    @gScore.setter
    def gScore(self, value: float):
        self.__gScore = value
        self._property_changed('gScore')        

    @property
    def marketValue(self) -> float:
        """Marketable value of a given position, generally the market price for a given date."""
        return self.__marketValue

    @marketValue.setter
    def marketValue(self, value: float):
        self.__marketValue = value
        self._property_changed('marketValue')        

    @property
    def multipleScore(self) -> float:
        """Multiple percentile relative to Americas coverage universe (a higher score means more expensive)."""
        return self.__multipleScore

    @multipleScore.setter
    def multipleScore(self, value: float):
        self.__multipleScore = value
        self._property_changed('multipleScore')        

    @property
    def lendingFundNav(self) -> float:
        """Net Asset Value of a securities lending fund."""
        return self.__lendingFundNav

    @lendingFundNav.setter
    def lendingFundNav(self, value: float):
        self.__lendingFundNav = value
        self._property_changed('lendingFundNav')        

    @property
    def sourceOriginalCategory(self) -> str:
        """Source category's original name."""
        return self.__sourceOriginalCategory

    @sourceOriginalCategory.setter
    def sourceOriginalCategory(self, value: str):
        self.__sourceOriginalCategory = value
        self._property_changed('sourceOriginalCategory')        

    @property
    def betaAdjustedExposure(self) -> float:
        """Beta adjusted exposure."""
        return self.__betaAdjustedExposure

    @betaAdjustedExposure.setter
    def betaAdjustedExposure(self, value: float):
        self.__betaAdjustedExposure = value
        self._property_changed('betaAdjustedExposure')        

    @property
    def composite5DayAdv(self) -> float:
        """Composite 5 day ADV."""
        return self.__composite5DayAdv

    @composite5DayAdv.setter
    def composite5DayAdv(self, value: float):
        self.__composite5DayAdv = value
        self._property_changed('composite5DayAdv')        

    @property
    def latestExecutionTime(self) -> datetime.datetime:
        """ISO 8601-formatted timestamp"""
        return self.__latestExecutionTime

    @latestExecutionTime.setter
    def latestExecutionTime(self, value: datetime.datetime):
        self.__latestExecutionTime = value
        self._property_changed('latestExecutionTime')        

    @property
    def dividendPoints(self) -> float:
        """Expected Dividend in index points."""
        return self.__dividendPoints

    @dividendPoints.setter
    def dividendPoints(self, value: float):
        self.__dividendPoints = value
        self._property_changed('dividendPoints')        

    @property
    def newIdeasWtd(self) -> float:
        """Ideas received by clients Week to date."""
        return self.__newIdeasWtd

    @newIdeasWtd.setter
    def newIdeasWtd(self, value: float):
        self.__newIdeasWtd = value
        self._property_changed('newIdeasWtd')        

    @property
    def paid(self) -> float:
        """Number of trades paid."""
        return self.__paid

    @paid.setter
    def paid(self, value: float):
        self.__paid = value
        self._property_changed('paid')        

    @property
    def short(self) -> float:
        """Short exposure."""
        return self.__short

    @short.setter
    def short(self, value: float):
        self.__short = value
        self._property_changed('short')        

    @property
    def location(self) -> str:
        """The location at which a price fixing has been taken."""
        return self.__location

    @location.setter
    def location(self, value: str):
        self.__location = value
        self._property_changed('location')        

    @property
    def comment(self) -> str:
        """The comment associated with the trade idea in URL encoded format."""
        return self.__comment

    @comment.setter
    def comment(self, value: str):
        self.__comment = value
        self._property_changed('comment')        

    @property
    def bosInTicksDescription(self) -> str:
        """Description of the Stock's Bid-Offer Spread in Ticks on the particular date."""
        return self.__bosInTicksDescription

    @bosInTicksDescription.setter
    def bosInTicksDescription(self, value: str):
        self.__bosInTicksDescription = value
        self._property_changed('bosInTicksDescription')        

    @property
    def sourceSymbol(self) -> str:
        """Source symbol."""
        return self.__sourceSymbol

    @sourceSymbol.setter
    def sourceSymbol(self, value: str):
        self.__sourceSymbol = value
        self._property_changed('sourceSymbol')        

    @property
    def time(self) -> datetime.datetime:
        """ISO 8601 formatted date and time."""
        return self.__time

    @time.setter
    def time(self, value: datetime.datetime):
        self.__time = value
        self._property_changed('time')        

    @property
    def scenarioId(self) -> str:
        """Marquee unique scenario identifier"""
        return self.__scenarioId

    @scenarioId.setter
    def scenarioId(self, value: str):
        self.__scenarioId = value
        self._property_changed('scenarioId')        

    @property
    def askUnadjusted(self) -> float:
        """Unadjusted ask level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__askUnadjusted

    @askUnadjusted.setter
    def askUnadjusted(self, value: float):
        self.__askUnadjusted = value
        self._property_changed('askUnadjusted')        

    @property
    def queueClockTime(self) -> float:
        """The Queue Clock Time of the stock  on the particular date."""
        return self.__queueClockTime

    @queueClockTime.setter
    def queueClockTime(self, value: float):
        self.__queueClockTime = value
        self._property_changed('queueClockTime')        

    @property
    def askChange(self) -> float:
        """Change in the ask price."""
        return self.__askChange

    @askChange.setter
    def askChange(self, value: float):
        self.__askChange = value
        self._property_changed('askChange')        

    @property
    def impliedCorrelation(self) -> float:
        """Correlation of an asset implied by observations of market prices."""
        return self.__impliedCorrelation

    @impliedCorrelation.setter
    def impliedCorrelation(self, value: float):
        self.__impliedCorrelation = value
        self._property_changed('impliedCorrelation')        

    @property
    def tcmCostParticipationRate50Pct(self) -> float:
        """TCM cost with a 50 percent participation rate."""
        return self.__tcmCostParticipationRate50Pct

    @tcmCostParticipationRate50Pct.setter
    def tcmCostParticipationRate50Pct(self, value: float):
        self.__tcmCostParticipationRate50Pct = value
        self._property_changed('tcmCostParticipationRate50Pct')        

    @property
    def normalizedPerformance(self) -> float:
        """Performance that is normalized to 1."""
        return self.__normalizedPerformance

    @normalizedPerformance.setter
    def normalizedPerformance(self, value: float):
        self.__normalizedPerformance = value
        self._property_changed('normalizedPerformance')        

    @property
    def cmId(self) -> str:
        """Prime Client Master Party Id."""
        return self.__cmId

    @cmId.setter
    def cmId(self, value: str):
        self.__cmId = value
        self._property_changed('cmId')        

    @property
    def type(self) -> str:
        """Asset type differentiates the product categorization or contract type"""
        return self.__type

    @type.setter
    def type(self, value: str):
        self.__type = value
        self._property_changed('type')        

    @property
    def mdapi(self) -> str:
        """MDAPI Asset."""
        return self.__mdapi

    @mdapi.setter
    def mdapi(self, value: str):
        self.__mdapi = value
        self._property_changed('mdapi')        

    @property
    def dividendYield(self) -> float:
        """Annualized Dividend Yield."""
        return self.__dividendYield

    @dividendYield.setter
    def dividendYield(self, value: float):
        self.__dividendYield = value
        self._property_changed('dividendYield')        

    @property
    def cumulativePnl(self) -> float:
        """Cumulative PnL from the start date to the current date."""
        return self.__cumulativePnl

    @cumulativePnl.setter
    def cumulativePnl(self, value: float):
        self.__cumulativePnl = value
        self._property_changed('cumulativePnl')        

    @property
    def sourceOrigin(self) -> str:
        """Source origin."""
        return self.__sourceOrigin

    @sourceOrigin.setter
    def sourceOrigin(self, value: str):
        self.__sourceOrigin = value
        self._property_changed('sourceOrigin')        

    @property
    def shortTenor(self) -> str:
        """Tenor of instrument."""
        return self.__shortTenor

    @shortTenor.setter
    def shortTenor(self, value: str):
        self.__shortTenor = value
        self._property_changed('shortTenor')        

    @property
    def loss(self) -> float:
        """Loss price component."""
        return self.__loss

    @loss.setter
    def loss(self, value: float):
        self.__loss = value
        self._property_changed('loss')        

    @property
    def unadjustedVolume(self) -> float:
        """Unadjusted volume traded."""
        return self.__unadjustedVolume

    @unadjustedVolume.setter
    def unadjustedVolume(self, value: float):
        self.__unadjustedVolume = value
        self._property_changed('unadjustedVolume')        

    @property
    def measures(self) -> Tuple[str, ...]:
        """Fields that are nullable."""
        return self.__measures

    @measures.setter
    def measures(self, value: Tuple[str, ...]):
        self.__measures = value
        self._property_changed('measures')        

    @property
    def tradingCostPnl(self) -> float:
        """Trading cost profit and loss (PNL)."""
        return self.__tradingCostPnl

    @tradingCostPnl.setter
    def tradingCostPnl(self, value: float):
        self.__tradingCostPnl = value
        self._property_changed('tradingCostPnl')        

    @property
    def internalUser(self) -> bool:
        """Whether user is internal or not."""
        return self.__internalUser

    @internalUser.setter
    def internalUser(self, value: bool):
        self.__internalUser = value
        self._property_changed('internalUser')        

    @property
    def price(self) -> float:
        """Price of instrument."""
        return self.__price

    @price.setter
    def price(self, value: float):
        self.__price = value
        self._property_changed('price')        

    @property
    def paymentQuantity(self) -> float:
        """Quantity in the payment currency."""
        return self.__paymentQuantity

    @paymentQuantity.setter
    def paymentQuantity(self, value: float):
        self.__paymentQuantity = value
        self._property_changed('paymentQuantity')        

    @property
    def underlyer(self) -> str:
        """The underlyer of the security. The cross for FX forwards, for example."""
        return self.__underlyer

    @underlyer.setter
    def underlyer(self, value: str):
        self.__underlyer = value
        self._property_changed('underlyer')        

    @property
    def createdTime(self) -> datetime.datetime:
        """Time created. ISO 8601 formatted string"""
        return self.__createdTime

    @createdTime.setter
    def createdTime(self, value: datetime.datetime):
        self.__createdTime = value
        self._property_changed('createdTime')        

    @property
    def positionIdx(self) -> int:
        """The index of the corresponding position in the risk request."""
        return self.__positionIdx

    @positionIdx.setter
    def positionIdx(self, value: int):
        self.__positionIdx = value
        self._property_changed('positionIdx')        

    @property
    def secName(self) -> str:
        """Internal Goldman Sachs security name."""
        return self.__secName

    @secName.setter
    def secName(self, value: str):
        self.__secName = value
        self._property_changed('secName')        

    @property
    def percentADV(self) -> float:
        """Size of trade as percentage of average daily volume (e.g. .05, 1, 2, ..., 20)."""
        return self.__percentADV

    @percentADV.setter
    def percentADV(self, value: float):
        self.__percentADV = value
        self._property_changed('percentADV')        

    @property
    def redemptionOption(self) -> str:
        """Indicates the calculation convention for callable instruments."""
        return self.__redemptionOption

    @redemptionOption.setter
    def redemptionOption(self, value: str):
        self.__redemptionOption = value
        self._property_changed('redemptionOption')        

    @property
    def unadjustedLow(self) -> float:
        """Unadjusted low level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__unadjustedLow

    @unadjustedLow.setter
    def unadjustedLow(self, value: float):
        self.__unadjustedLow = value
        self._property_changed('unadjustedLow')        

    @property
    def contract(self) -> str:
        """Contract month code and year (e.g. F18)."""
        return self.__contract

    @contract.setter
    def contract(self, value: str):
        self.__contract = value
        self._property_changed('contract')        

    @property
    def sedol(self) -> str:
        """SEDOL - Stock Exchange Daily Official List (subject to licensing)."""
        return self.__sedol

    @sedol.setter
    def sedol(self, value: str):
        self.__sedol = value
        self._property_changed('sedol')        

    @property
    def roundingCostPnl(self) -> float:
        """Rounding Cost Profit and Loss."""
        return self.__roundingCostPnl

    @roundingCostPnl.setter
    def roundingCostPnl(self, value: float):
        self.__roundingCostPnl = value
        self._property_changed('roundingCostPnl')        

    @property
    def sustainGlobal(self) -> bool:
        """True if the stock is on the SUSTAIN (Global) 50 list as of the corresponding date. False if the stock is removed from the SUSTAIN (Global) 50 list on the corresponding date."""
        return self.__sustainGlobal

    @sustainGlobal.setter
    def sustainGlobal(self, value: bool):
        self.__sustainGlobal = value
        self._property_changed('sustainGlobal')        

    @property
    def sourceTicker(self) -> str:
        """Source ticker."""
        return self.__sourceTicker

    @sourceTicker.setter
    def sourceTicker(self, value: str):
        self.__sourceTicker = value
        self._property_changed('sourceTicker')        

    @property
    def portfolioId(self) -> str:
        """Marquee unique identifier for a portfolio."""
        return self.__portfolioId

    @portfolioId.setter
    def portfolioId(self, value: str):
        self.__portfolioId = value
        self._property_changed('portfolioId')        

    @property
    def gsid(self) -> str:
        """Goldman Sachs internal equity identifier."""
        return self.__gsid

    @gsid.setter
    def gsid(self, value: str):
        self.__gsid = value
        self._property_changed('gsid')        

    @property
    def esPercentile(self) -> float:
        """Sector relative percentile based on E&S score."""
        return self.__esPercentile

    @esPercentile.setter
    def esPercentile(self, value: float):
        self.__esPercentile = value
        self._property_changed('esPercentile')        

    @property
    def lendingFund(self) -> str:
        """Name of the lending fund on a securities lending agreement."""
        return self.__lendingFund

    @lendingFund.setter
    def lendingFund(self, value: str):
        self.__lendingFund = value
        self._property_changed('lendingFund')        

    @property
    def tcmCostParticipationRate15Pct(self) -> float:
        """TCM cost with a 15 percent participation rate."""
        return self.__tcmCostParticipationRate15Pct

    @tcmCostParticipationRate15Pct.setter
    def tcmCostParticipationRate15Pct(self, value: float):
        self.__tcmCostParticipationRate15Pct = value
        self._property_changed('tcmCostParticipationRate15Pct')        

    @property
    def sensitivity(self) -> float:
        """Sensitivity."""
        return self.__sensitivity

    @sensitivity.setter
    def sensitivity(self, value: float):
        self.__sensitivity = value
        self._property_changed('sensitivity')        

    @property
    def fiscalYear(self) -> str:
        """The Calendar Year."""
        return self.__fiscalYear

    @fiscalYear.setter
    def fiscalYear(self, value: str):
        self.__fiscalYear = value
        self._property_changed('fiscalYear')        

    @property
    def recallDate(self) -> datetime.date:
        """The date at which the securities on loan were recalled."""
        return self.__recallDate

    @recallDate.setter
    def recallDate(self, value: datetime.date):
        self.__recallDate = value
        self._property_changed('recallDate')        

    @property
    def rcic(self) -> str:
        """Reuters composite instrument code (subject to licensing)."""
        return self.__rcic

    @rcic.setter
    def rcic(self, value: str):
        self.__rcic = value
        self._property_changed('rcic')        

    @property
    def simonAssetTags(self) -> Tuple[str, ...]:
        """SIMON Asset Tags."""
        return self.__simonAssetTags

    @simonAssetTags.setter
    def simonAssetTags(self, value: Tuple[str, ...]):
        self.__simonAssetTags = value
        self._property_changed('simonAssetTags')        

    @property
    def internal(self) -> bool:
        """Whether request came from internal or external."""
        return self.__internal

    @internal.setter
    def internal(self, value: bool):
        self.__internal = value
        self._property_changed('internal')        

    @property
    def forwardPoint(self) -> float:
        """Outright forward minus spot."""
        return self.__forwardPoint

    @forwardPoint.setter
    def forwardPoint(self, value: float):
        self.__forwardPoint = value
        self._property_changed('forwardPoint')        

    @property
    def assetClassificationsGicsIndustry(self) -> str:
        """GICS Industry classification (level 3)."""
        return self.__assetClassificationsGicsIndustry

    @assetClassificationsGicsIndustry.setter
    def assetClassificationsGicsIndustry(self, value: str):
        self.__assetClassificationsGicsIndustry = value
        self._property_changed('assetClassificationsGicsIndustry')        

    @property
    def adjustedBidPrice(self) -> float:
        """Latest Bid Price (price willing to buy) adjusted for corporate actions."""
        return self.__adjustedBidPrice

    @adjustedBidPrice.setter
    def adjustedBidPrice(self, value: float):
        self.__adjustedBidPrice = value
        self._property_changed('adjustedBidPrice')        

    @property
    def hitRateQtd(self) -> float:
        """Hit Rate Ratio Quarter to Date."""
        return self.__hitRateQtd

    @hitRateQtd.setter
    def hitRateQtd(self, value: float):
        self.__hitRateQtd = value
        self._property_changed('hitRateQtd')        

    @property
    def varSwap(self) -> float:
        """Strike such that the price of an uncapped variance swap on the underlying index is zero at inception."""
        return self.__varSwap

    @varSwap.setter
    def varSwap(self, value: float):
        self.__varSwap = value
        self._property_changed('varSwap')        

    @property
    def lowUnadjusted(self) -> float:
        """Unadjusted low level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__lowUnadjusted

    @lowUnadjusted.setter
    def lowUnadjusted(self, value: float):
        self.__lowUnadjusted = value
        self._property_changed('lowUnadjusted')        

    @property
    def sectorsRaw(self) -> Tuple[str, ...]:
        """Sector classifications of an asset."""
        return self.__sectorsRaw

    @sectorsRaw.setter
    def sectorsRaw(self, value: Tuple[str, ...]):
        self.__sectorsRaw = value
        self._property_changed('sectorsRaw')        

    @property
    def recallQuantity(self) -> float:
        """Defines the amount of shares being recalled in a stock loan recall activity."""
        return self.__recallQuantity

    @recallQuantity.setter
    def recallQuantity(self, value: float):
        self.__recallQuantity = value
        self._property_changed('recallQuantity')        

    @property
    def low(self) -> float:
        """Low level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__low

    @low.setter
    def low(self, value: float):
        self.__low = value
        self._property_changed('low')        

    @property
    def crossGroup(self) -> str:
        """Economic cross groupings."""
        return self.__crossGroup

    @crossGroup.setter
    def crossGroup(self, value: str):
        self.__crossGroup = value
        self._property_changed('crossGroup')        

    @property
    def integratedScore(self) -> float:
        """Average of the Growth, Financial Returns and (1-Multiple) percentile (a higher score means more attractive)."""
        return self.__integratedScore

    @integratedScore.setter
    def integratedScore(self, value: float):
        self.__integratedScore = value
        self._property_changed('integratedScore')        

    @property
    def reportRunTime(self) -> datetime.datetime:
        """Time that the report was run."""
        return self.__reportRunTime

    @reportRunTime.setter
    def reportRunTime(self, value: datetime.datetime):
        self.__reportRunTime = value
        self._property_changed('reportRunTime')        

    @property
    def fiveDayPriceChangeBps(self) -> float:
        """The five day movement in price measured in basis points."""
        return self.__fiveDayPriceChangeBps

    @fiveDayPriceChangeBps.setter
    def fiveDayPriceChangeBps(self, value: float):
        self.__fiveDayPriceChangeBps = value
        self._property_changed('fiveDayPriceChangeBps')        

    @property
    def tradeSize(self) -> float:
        """Size of trade ($mm)."""
        return self.__tradeSize

    @tradeSize.setter
    def tradeSize(self, value: float):
        self.__tradeSize = value
        self._property_changed('tradeSize')        

    @property
    def holdings(self) -> float:
        """Number of units of a given asset held within a portfolio."""
        return self.__holdings

    @holdings.setter
    def holdings(self, value: float):
        self.__holdings = value
        self._property_changed('holdings')        

    @property
    def symbolDimensions(self) -> Tuple[str, ...]:
        """Set of fields that determine database table name."""
        return self.__symbolDimensions

    @symbolDimensions.setter
    def symbolDimensions(self, value: Tuple[str, ...]):
        self.__symbolDimensions = value
        self._property_changed('symbolDimensions')        

    @property
    def priceMethod(self) -> str:
        """Method used to calculate net price."""
        return self.__priceMethod

    @priceMethod.setter
    def priceMethod(self, value: str):
        self.__priceMethod = value
        self._property_changed('priceMethod')        

    @property
    def quotingStyle(self) -> str:
        return self.__quotingStyle

    @quotingStyle.setter
    def quotingStyle(self, value: str):
        self.__quotingStyle = value
        self._property_changed('quotingStyle')        

    @property
    def scenarioGroupId(self) -> str:
        """Marquee unique scenario group identifier"""
        return self.__scenarioGroupId

    @scenarioGroupId.setter
    def scenarioGroupId(self, value: str):
        self.__scenarioGroupId = value
        self._property_changed('scenarioGroupId')        

    @property
    def errorMessage(self) -> str:
        """Error message to correspond to error in factor field."""
        return self.__errorMessage

    @errorMessage.setter
    def errorMessage(self, value: str):
        self.__errorMessage = value
        self._property_changed('errorMessage')        

    @property
    def averageImpliedVariance(self) -> float:
        """Average variance of an asset implied by observations of market prices."""
        return self.__averageImpliedVariance

    @averageImpliedVariance.setter
    def averageImpliedVariance(self, value: float):
        self.__averageImpliedVariance = value
        self._property_changed('averageImpliedVariance')        

    @property
    def avgTradeRateDescription(self) -> str:
        """Description of the Stock's Average Trading Rate on the particular date."""
        return self.__avgTradeRateDescription

    @avgTradeRateDescription.setter
    def avgTradeRateDescription(self, value: str):
        self.__avgTradeRateDescription = value
        self._property_changed('avgTradeRateDescription')        

    @property
    def midPrice(self) -> float:
        """The mid price."""
        return self.__midPrice

    @midPrice.setter
    def midPrice(self, value: float):
        self.__midPrice = value
        self._property_changed('midPrice')        

    @property
    def fraction(self) -> float:
        """Fraction."""
        return self.__fraction

    @fraction.setter
    def fraction(self, value: float):
        self.__fraction = value
        self._property_changed('fraction')        

    @property
    def stsCreditMarket(self) -> str:
        """Credit risk market."""
        return self.__stsCreditMarket

    @stsCreditMarket.setter
    def stsCreditMarket(self, value: str):
        self.__stsCreditMarket = value
        self._property_changed('stsCreditMarket')        

    @property
    def assetCountShort(self) -> float:
        """Number of assets in a portfolio with short exposure."""
        return self.__assetCountShort

    @assetCountShort.setter
    def assetCountShort(self, value: float):
        self.__assetCountShort = value
        self._property_changed('assetCountShort')        

    @property
    def stsEmDm(self) -> str:
        """Emerging or developed market classification."""
        return self.__stsEmDm

    @stsEmDm.setter
    def stsEmDm(self, value: str):
        self.__stsEmDm = value
        self._property_changed('stsEmDm')        

    @property
    def requiredCollateralValue(self) -> float:
        """Amount of collateral required to cover contractual obligation."""
        return self.__requiredCollateralValue

    @requiredCollateralValue.setter
    def requiredCollateralValue(self, value: float):
        self.__requiredCollateralValue = value
        self._property_changed('requiredCollateralValue')        

    @property
    def tcmCostHorizon2Day(self) -> float:
        """TCM cost with a 2 day time horizon."""
        return self.__tcmCostHorizon2Day

    @tcmCostHorizon2Day.setter
    def tcmCostHorizon2Day(self, value: float):
        self.__tcmCostHorizon2Day = value
        self._property_changed('tcmCostHorizon2Day')        

    @property
    def pendingLoanCount(self) -> float:
        """The number of pending loans that exist on a given date."""
        return self.__pendingLoanCount

    @pendingLoanCount.setter
    def pendingLoanCount(self, value: float):
        self.__pendingLoanCount = value
        self._property_changed('pendingLoanCount')        

    @property
    def queueInLots(self) -> float:
        """The Queue size in Lots (if applicable) of the stock  on the particular date."""
        return self.__queueInLots

    @queueInLots.setter
    def queueInLots(self, value: float):
        self.__queueInLots = value
        self._property_changed('queueInLots')        

    @property
    def priceRangeInTicksDescription(self) -> str:
        """Description of the Stock's Price Range in Ticks on the particular date."""
        return self.__priceRangeInTicksDescription

    @priceRangeInTicksDescription.setter
    def priceRangeInTicksDescription(self, value: str):
        self.__priceRangeInTicksDescription = value
        self._property_changed('priceRangeInTicksDescription')        

    @property
    def date(self) -> datetime.date:
        """ISO 8601 formatted date."""
        return self.__date

    @date.setter
    def date(self, value: datetime.date):
        self.__date = value
        self._property_changed('date')        

    @property
    def tenderOfferExpirationDate(self) -> str:
        """Expiration date of the tender offer."""
        return self.__tenderOfferExpirationDate

    @tenderOfferExpirationDate.setter
    def tenderOfferExpirationDate(self, value: str):
        self.__tenderOfferExpirationDate = value
        self._property_changed('tenderOfferExpirationDate')        

    @property
    def highUnadjusted(self) -> float:
        """Unadjusted high level of an asset based on official exchange fixing or calculation agent marked level."""
        return self.__highUnadjusted

    @highUnadjusted.setter
    def highUnadjusted(self, value: float):
        self.__highUnadjusted = value
        self._property_changed('highUnadjusted')        

    @property
    def sourceCategory(self) -> str:
        """Source category of event."""
        return self.__sourceCategory

    @sourceCategory.setter
    def sourceCategory(self, value: str):
        self.__sourceCategory = value
        self._property_changed('sourceCategory')        

    @property
    def volumeUnadjusted(self) -> float:
        """Unadjusted volume traded."""
        return self.__volumeUnadjusted

    @volumeUnadjusted.setter
    def volumeUnadjusted(self, value: float):
        self.__volumeUnadjusted = value
        self._property_changed('volumeUnadjusted')        

    @property
    def avgTradeRateLabel(self):
        """Label of the Stock's Average Trading Rate on the particular date."""
        return self.__avgTradeRateLabel

    @avgTradeRateLabel.setter
    def avgTradeRateLabel(self, value):
        self.__avgTradeRateLabel = value
        self._property_changed('avgTradeRateLabel')        

    @property
    def tcmCostParticipationRate5Pct(self) -> float:
        """TCM cost with a 5 percent participation rate."""
        return self.__tcmCostParticipationRate5Pct

    @tcmCostParticipationRate5Pct.setter
    def tcmCostParticipationRate5Pct(self, value: float):
        self.__tcmCostParticipationRate5Pct = value
        self._property_changed('tcmCostParticipationRate5Pct')        

    @property
    def isActive(self) -> bool:
        """Whether this entry is active."""
        return self.__isActive

    @isActive.setter
    def isActive(self, value: bool):
        self.__isActive = value
        self._property_changed('isActive')        

    @property
    def growthScore(self) -> float:
        """Growth percentile relative to Americas coverage universe (a higher score means faster growth)."""
        return self.__growthScore

    @growthScore.setter
    def growthScore(self, value: float):
        self.__growthScore = value
        self._property_changed('growthScore')        

    @property
    def bufferThreshold(self) -> float:
        """The required buffer between holdings and on loan quantity for an asset."""
        return self.__bufferThreshold

    @bufferThreshold.setter
    def bufferThreshold(self, value: float):
        self.__bufferThreshold = value
        self._property_changed('bufferThreshold')        

    @property
    def encodedStats(self) -> str:
        """Asset stats object in json format."""
        return self.__encodedStats

    @encodedStats.setter
    def encodedStats(self, value: str):
        self.__encodedStats = value
        self._property_changed('encodedStats')        

    @property
    def adjustedShortInterest(self) -> float:
        """Adjusted Short Interest rate."""
        return self.__adjustedShortInterest

    @adjustedShortInterest.setter
    def adjustedShortInterest(self, value: float):
        self.__adjustedShortInterest = value
        self._property_changed('adjustedShortInterest')        

    @property
    def askSize(self) -> float:
        """The number of shares, lots, or contracts willing to sell at the Ask price."""
        return self.__askSize

    @askSize.setter
    def askSize(self, value: float):
        self.__askSize = value
        self._property_changed('askSize')        

    @property
    def mdapiType(self) -> str:
        """The MDAPI data type - DEPRECATED."""
        return self.__mdapiType

    @mdapiType.setter
    def mdapiType(self, value: str):
        self.__mdapiType = value
        self._property_changed('mdapiType')        

    @property
    def group(self) -> str:
        """Region or sector following the MSCI Global Industry Classification Standard (GICS)."""
        return self.__group

    @group.setter
    def group(self, value: str):
        self.__group = value
        self._property_changed('group')        

    @property
    def estimatedSpread(self) -> float:
        """Average bid-ask quoted spread of the stock (bps) over the execution horizon (1 day)."""
        return self.__estimatedSpread

    @estimatedSpread.setter
    def estimatedSpread(self, value: float):
        self.__estimatedSpread = value
        self._property_changed('estimatedSpread')        

    @property
    def resource(self) -> str:
        """The event resource. For example: Asset"""
        return self.__resource

    @resource.setter
    def resource(self, value: str):
        self.__resource = value
        self._property_changed('resource')        

    @property
    def created(self) -> datetime.datetime:
        """Created time."""
        return self.__created

    @created.setter
    def created(self, value: datetime.datetime):
        self.__created = value
        self._property_changed('created')        

    @property
    def averageRealizedVolatility(self) -> float:
        """Average volatility of an asset realized by observations of market prices."""
        return self.__averageRealizedVolatility

    @averageRealizedVolatility.setter
    def averageRealizedVolatility(self, value: float):
        self.__averageRealizedVolatility = value
        self._property_changed('averageRealizedVolatility')        

    @property
    def tcmCost(self) -> float:
        """Pretrade computation of trading out cost."""
        return self.__tcmCost

    @tcmCost.setter
    def tcmCost(self, value: float):
        self.__tcmCost = value
        self._property_changed('tcmCost')        

    @property
    def sustainJapan(self) -> bool:
        """True if the stock is on the SUSTAIN Japan list as of the corresponding date. False if the stock is removed from the SUSTAIN Japan list on the corresponding date."""
        return self.__sustainJapan

    @sustainJapan.setter
    def sustainJapan(self, value: bool):
        self.__sustainJapan = value
        self._property_changed('sustainJapan')        

    @property
    def navSpread(self) -> float:
        """Net asset value spread. Quoted (running) spread (mid) of the underlying basket of single name CDS. (Theoretical Index value). In basis points."""
        return self.__navSpread

    @navSpread.setter
    def navSpread(self, value: float):
        self.__navSpread = value
        self._property_changed('navSpread')        

    @property
    def bidPrice(self) -> float:
        """Latest Bid Price (price willing to buy)."""
        return self.__bidPrice

    @bidPrice.setter
    def bidPrice(self, value: float):
        self.__bidPrice = value
        self._property_changed('bidPrice')        

    @property
    def dollarTotalReturn(self) -> float:
        """The dollar total return of an instrument."""
        return self.__dollarTotalReturn

    @dollarTotalReturn.setter
    def dollarTotalReturn(self, value: float):
        self.__dollarTotalReturn = value
        self._property_changed('dollarTotalReturn')        

    @property
    def hedgeTrackingError(self) -> float:
        """Standard deviation of the difference in the portfolio and benchmark returns over time."""
        return self.__hedgeTrackingError

    @hedgeTrackingError.setter
    def hedgeTrackingError(self, value: float):
        self.__hedgeTrackingError = value
        self._property_changed('hedgeTrackingError')        

    @property
    def marketCapCategory(self) -> str:
        """Category of market capitalizations a fund is focused on from an investment perspective. Same view permissions as the asset."""
        return self.__marketCapCategory

    @marketCapCategory.setter
    def marketCapCategory(self, value: str):
        self.__marketCapCategory = value
        self._property_changed('marketCapCategory')        

    @property
    def historicalVolume(self) -> float:
        """One month rolling average."""
        return self.__historicalVolume

    @historicalVolume.setter
    def historicalVolume(self, value: float):
        self.__historicalVolume = value
        self._property_changed('historicalVolume')        

    @property
    def esNumericPercentile(self) -> float:
        """Sector relative percentile based on E&S numeric score."""
        return self.__esNumericPercentile

    @esNumericPercentile.setter
    def esNumericPercentile(self, value: float):
        self.__esNumericPercentile = value
        self._property_changed('esNumericPercentile')        

    @property
    def strikePrice(self) -> float:
        """Strike price."""
        return self.__strikePrice

    @strikePrice.setter
    def strikePrice(self, value: float):
        self.__strikePrice = value
        self._property_changed('strikePrice')        

    @property
    def eventStartDate(self) -> datetime.date:
        """The start date of the event if the event occurs during a time window, in the time zone of the exchange where the company is listed (optional)."""
        return self.__eventStartDate

    @eventStartDate.setter
    def eventStartDate(self, value: datetime.date):
        self.__eventStartDate = value
        self._property_changed('eventStartDate')        

    @property
    def askGspread(self) -> float:
        """Ask G spread."""
        return self.__askGspread

    @askGspread.setter
    def askGspread(self, value: float):
        self.__askGspread = value
        self._property_changed('askGspread')        

    @property
    def calSpreadMisPricing(self) -> float:
        """Futures implied funding rate relative to interest rate benchmark (usually Libor-based). Represents dividend-adjusted rate at which investor is borrowing (lending) when long (short) future."""
        return self.__calSpreadMisPricing

    @calSpreadMisPricing.setter
    def calSpreadMisPricing(self, value: float):
        self.__calSpreadMisPricing = value
        self._property_changed('calSpreadMisPricing')        

    @property
    def equityGamma(self) -> float:
        """Gamma exposure to equity products."""
        return self.__equityGamma

    @equityGamma.setter
    def equityGamma(self, value: float):
        self.__equityGamma = value
        self._property_changed('equityGamma')        

    @property
    def grossIncome(self) -> float:
        return self.__grossIncome

    @grossIncome.setter
    def grossIncome(self, value: float):
        self.__grossIncome = value
        self._property_changed('grossIncome')        

    @property
    def emId(self) -> str:
        """Entity Master identifier."""
        return self.__emId

    @emId.setter
    def emId(self, value: str):
        self.__emId = value
        self._property_changed('emId')        

    @property
    def adjustedOpenPrice(self) -> float:
        """Opening level of an asset based on official exchange fixing or calculation agent marked level adjusted for corporate actions."""
        return self.__adjustedOpenPrice

    @adjustedOpenPrice.setter
    def adjustedOpenPrice(self, value: float):
        self.__adjustedOpenPrice = value
        self._property_changed('adjustedOpenPrice')        

    @property
    def assetCountInModel(self) -> float:
        """Number of assets in a portfolio in a given risk model."""
        return self.__assetCountInModel

    @assetCountInModel.setter
    def assetCountInModel(self, value: float):
        self.__assetCountInModel = value
        self._property_changed('assetCountInModel')        

    @property
    def stsCreditRegion(self) -> str:
        """Credit risk region."""
        return self.__stsCreditRegion

    @stsCreditRegion.setter
    def stsCreditRegion(self, value: str):
        self.__stsCreditRegion = value
        self._property_changed('stsCreditRegion')        

    @property
    def point(self) -> str:
        """MDAPI point."""
        return self.__point

    @point.setter
    def point(self, value: str):
        self.__point = value
        self._property_changed('point')        

    @property
    def totalReturns(self) -> float:
        """Total returns for backtest."""
        return self.__totalReturns

    @totalReturns.setter
    def totalReturns(self, value: float):
        self.__totalReturns = value
        self._property_changed('totalReturns')        

    @property
    def lender(self) -> str:
        """Name of the lending entity on a securities lending agreement."""
        return self.__lender

    @lender.setter
    def lender(self, value: str):
        self.__lender = value
        self._property_changed('lender')        

    @property
    def minTemperature(self) -> float:
        """Minimum temperature observed on a given day in fahrenheit."""
        return self.__minTemperature

    @minTemperature.setter
    def minTemperature(self, value: float):
        self.__minTemperature = value
        self._property_changed('minTemperature')        

    @property
    def closeTime(self) -> datetime.datetime:
        """Time closed. ISO 8601 formatted string."""
        return self.__closeTime

    @closeTime.setter
    def closeTime(self, value: datetime.datetime):
        self.__closeTime = value
        self._property_changed('closeTime')        

    @property
    def value(self) -> float:
        """The given value."""
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value
        self._property_changed('value')        

    @property
    def relativeStrike(self) -> float:
        """Strike relative to spot or forward level in terms of percent of either spot or forward level."""
        return self.__relativeStrike

    @relativeStrike.setter
    def relativeStrike(self, value: float):
        self.__relativeStrike = value
        self._property_changed('relativeStrike')        

    @property
    def amount(self) -> float:
        """Amount corporate actions pay out."""
        return self.__amount

    @amount.setter
    def amount(self, value: float):
        self.__amount = value
        self._property_changed('amount')        

    @property
    def quantity(self) -> float:
        """Number of units of a given asset held within a portfolio."""
        return self.__quantity

    @quantity.setter
    def quantity(self, value: float):
        self.__quantity = value
        self._property_changed('quantity')        

    @property
    def lendingFundAcct(self) -> str:
        """Account associated with the securities lending fund."""
        return self.__lendingFundAcct

    @lendingFundAcct.setter
    def lendingFundAcct(self, value: str):
        self.__lendingFundAcct = value
        self._property_changed('lendingFundAcct')        

    @property
    def reportId(self) -> str:
        """Report Identifier."""
        return self.__reportId

    @reportId.setter
    def reportId(self, value: str):
        self.__reportId = value
        self._property_changed('reportId')        

    @property
    def indexWeight(self) -> float:
        """Weight of MSCI World positions in the region or sector (%)."""
        return self.__indexWeight

    @indexWeight.setter
    def indexWeight(self, value: float):
        self.__indexWeight = value
        self._property_changed('indexWeight')        

    @property
    def rebate(self) -> float:
        """Amount of the payment to an investor who puts up collateral in borrowing a stock."""
        return self.__rebate

    @rebate.setter
    def rebate(self, value: float):
        self.__rebate = value
        self._property_changed('rebate')        

    @property
    def flagship(self) -> bool:
        """Whether or not it is a flagship basket."""
        return self.__flagship

    @flagship.setter
    def flagship(self, value: bool):
        self.__flagship = value
        self._property_changed('flagship')        

    @property
    def trader(self) -> str:
        """Trader name."""
        return self.__trader

    @trader.setter
    def trader(self, value: str):
        self.__trader = value
        self._property_changed('trader')        

    @property
    def factorCategory(self) -> str:
        """Factor category."""
        return self.__factorCategory

    @factorCategory.setter
    def factorCategory(self, value: str):
        self.__factorCategory = value
        self._property_changed('factorCategory')        

    @property
    def impliedVolatility(self) -> float:
        """Volatility of an asset implied by observations of market prices."""
        return self.__impliedVolatility

    @impliedVolatility.setter
    def impliedVolatility(self, value: float):
        self.__impliedVolatility = value
        self._property_changed('impliedVolatility')        

    @property
    def spread(self) -> float:
        """Quoted (running) spread (mid) of buying / selling protection on an index. (Equally weighted CDS basket). In basis points."""
        return self.__spread

    @spread.setter
    def spread(self, value: float):
        self.__spread = value
        self._property_changed('spread')        

    @property
    def stsRatesMaturity(self) -> str:
        """Risk maturity bucket for STS assets."""
        return self.__stsRatesMaturity

    @stsRatesMaturity.setter
    def stsRatesMaturity(self, value: str):
        self.__stsRatesMaturity = value
        self._property_changed('stsRatesMaturity')        

    @property
    def equityDelta(self) -> float:
        """Delta exposure to equity products."""
        return self.__equityDelta

    @equityDelta.setter
    def equityDelta(self, value: float):
        self.__equityDelta = value
        self._property_changed('equityDelta')        

    @property
    def grossWeight(self) -> float:
        """Sum of the absolute weight values, which equals the sum of absolute long and short weights. If you have IBM stock with shortWeight 0.2 and also IBM stock with longWeight 0.4, then the grossWeight would be 0.6 (0.2+0.4)."""
        return self.__grossWeight

    @grossWeight.setter
    def grossWeight(self, value: float):
        self.__grossWeight = value
        self._property_changed('grossWeight')        

    @property
    def listed(self) -> bool:
        """Whether the asset is listed or not."""
        return self.__listed

    @listed.setter
    def listed(self, value: bool):
        self.__listed = value
        self._property_changed('listed')        

    @property
    def variance(self) -> float:
        """Market implied variance between two tenors."""
        return self.__variance

    @variance.setter
    def variance(self, value: float):
        self.__variance = value
        self._property_changed('variance')        

    @property
    def tcmCostHorizon6Hour(self) -> float:
        """TCM cost with a 6 hour time horizon."""
        return self.__tcmCostHorizon6Hour

    @tcmCostHorizon6Hour.setter
    def tcmCostHorizon6Hour(self, value: float):
        self.__tcmCostHorizon6Hour = value
        self._property_changed('tcmCostHorizon6Hour')        

    @property
    def g10Currency(self) -> bool:
        """Is a G10 asset."""
        return self.__g10Currency

    @g10Currency.setter
    def g10Currency(self, value: bool):
        self.__g10Currency = value
        self._property_changed('g10Currency')        

    @property
    def shockStyle(self) -> str:
        """Style of shocks to be used."""
        return self.__shockStyle

    @shockStyle.setter
    def shockStyle(self, value: str):
        self.__shockStyle = value
        self._property_changed('shockStyle')        

    @property
    def relativePeriod(self) -> str:
        """The relative period forward for which the forecast is available."""
        return self.__relativePeriod

    @relativePeriod.setter
    def relativePeriod(self, value: str):
        self.__relativePeriod = value
        self._property_changed('relativePeriod')        

    @property
    def isin(self) -> str:
        """ISIN - International securities identifier number (subect to licensing)."""
        return self.__isin

    @isin.setter
    def isin(self, value: str):
        self.__isin = value
        self._property_changed('isin')        

    @property
    def methodology(self) -> str:
        """Methodology of dataset."""
        return self.__methodology

    @methodology.setter
    def methodology(self, value: str):
        self.__methodology = value
        self._property_changed('methodology')        


class DataGroup(Base):
        
    """Dataset grouped by context (key dimensions)"""
       
    def __init__(self, ):
        super().__init__()
        


class DataQuery(Base):
               
    def __init__(self, id: str = None, dataSetId: str = None, format: Union[Format, str] = None, marketDataCoordinates: Tuple[MarketDataCoordinate, ...] = None, where: FieldFilterMap = None, vendor: str = None, startDate: datetime.date = None, endDate: datetime.date = None, startTime: datetime.datetime = None, endTime: datetime.datetime = None, asOfTime: datetime.datetime = None, idAsOfDate: datetime.date = None, since: datetime.datetime = None, dates: Tuple[datetime.date, ...] = None, times: Tuple[datetime.datetime, ...] = None, delay: int = None, intervals: int = None, pollingInterval: int = None, grouped: bool = None, fields: Tuple[Union[dict, str], ...] = None):
        super().__init__()
        self.__id = id
        self.__dataSetId = dataSetId
        self.__format = format if isinstance(format, Format) else get_enum_value(Format, format)
        self.__marketDataCoordinates = marketDataCoordinates
        self.__where = where
        self.__vendor = vendor
        self.__startDate = startDate
        self.__endDate = endDate
        self.__startTime = startTime
        self.__endTime = endTime
        self.__asOfTime = asOfTime
        self.__idAsOfDate = idAsOfDate
        self.__since = since
        self.__dates = dates
        self.__times = times
        self.__delay = delay
        self.__intervals = intervals
        self.__pollingInterval = pollingInterval
        self.__grouped = grouped
        self.__fields = fields

    @property
    def id(self) -> str:
        """Marquee unique identifier"""
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = value
        self._property_changed('id')        

    @property
    def dataSetId(self) -> str:
        """Marquee unique identifier"""
        return self.__dataSetId

    @dataSetId.setter
    def dataSetId(self, value: str):
        self.__dataSetId = value
        self._property_changed('dataSetId')        

    @property
    def format(self) -> Union[Format, str]:
        """Alternative format for data to be returned in"""
        return self.__format

    @format.setter
    def format(self, value: Union[Format, str]):
        self.__format = value if isinstance(value, Format) else get_enum_value(Format, value)
        self._property_changed('format')        

    @property
    def marketDataCoordinates(self) -> Tuple[MarketDataCoordinate, ...]:
        """Object representation of a market data coordinate"""
        return self.__marketDataCoordinates

    @marketDataCoordinates.setter
    def marketDataCoordinates(self, value: Tuple[MarketDataCoordinate, ...]):
        self.__marketDataCoordinates = value
        self._property_changed('marketDataCoordinates')        

    @property
    def where(self) -> FieldFilterMap:
        """Filters on data fields."""
        return self.__where

    @where.setter
    def where(self, value: FieldFilterMap):
        self.__where = value
        self._property_changed('where')        

    @property
    def vendor(self) -> str:
        return self.__vendor

    @vendor.setter
    def vendor(self, value: str):
        self.__vendor = value
        self._property_changed('vendor')        

    @property
    def startDate(self) -> datetime.date:
        """ISO 8601-formatted date"""
        return self.__startDate

    @startDate.setter
    def startDate(self, value: datetime.date):
        self.__startDate = value
        self._property_changed('startDate')        

    @property
    def endDate(self) -> datetime.date:
        """ISO 8601-formatted date"""
        return self.__endDate

    @endDate.setter
    def endDate(self, value: datetime.date):
        self.__endDate = value
        self._property_changed('endDate')        

    @property
    def startTime(self) -> datetime.datetime:
        """ISO 8601-formatted timestamp"""
        return self.__startTime

    @startTime.setter
    def startTime(self, value: datetime.datetime):
        self.__startTime = value
        self._property_changed('startTime')        

    @property
    def endTime(self) -> datetime.datetime:
        """ISO 8601-formatted timestamp"""
        return self.__endTime

    @endTime.setter
    def endTime(self, value: datetime.datetime):
        self.__endTime = value
        self._property_changed('endTime')        

    @property
    def asOfTime(self) -> datetime.datetime:
        """ISO 8601-formatted timestamp"""
        return self.__asOfTime

    @asOfTime.setter
    def asOfTime(self, value: datetime.datetime):
        self.__asOfTime = value
        self._property_changed('asOfTime')        

    @property
    def idAsOfDate(self) -> datetime.date:
        """ISO 8601-formatted date"""
        return self.__idAsOfDate

    @idAsOfDate.setter
    def idAsOfDate(self, value: datetime.date):
        self.__idAsOfDate = value
        self._property_changed('idAsOfDate')        

    @property
    def since(self) -> datetime.datetime:
        """ISO 8601-formatted timestamp"""
        return self.__since

    @since.setter
    def since(self, value: datetime.datetime):
        self.__since = value
        self._property_changed('since')        

    @property
    def dates(self) -> Tuple[datetime.date, ...]:
        """Select and return specific dates from dataset query results."""
        return self.__dates

    @dates.setter
    def dates(self, value: Tuple[datetime.date, ...]):
        self.__dates = value
        self._property_changed('dates')        

    @property
    def times(self) -> Tuple[datetime.datetime, ...]:
        """Select and return specific times from dataset query results."""
        return self.__times

    @times.setter
    def times(self, value: Tuple[datetime.datetime, ...]):
        self.__times = value
        self._property_changed('times')        

    @property
    def delay(self) -> int:
        """Number of minutes to delay returning data."""
        return self.__delay

    @delay.setter
    def delay(self, value: int):
        self.__delay = value
        self._property_changed('delay')        

    @property
    def intervals(self) -> int:
        """Number of intervals for which to return output times, for example if 10, it will return 10 data points evenly spaced over the time/date range."""
        return self.__intervals

    @intervals.setter
    def intervals(self, value: int):
        self.__intervals = value
        self._property_changed('intervals')        

    @property
    def pollingInterval(self) -> int:
        """When streaming, wait for this number of seconds between poll attempts."""
        return self.__pollingInterval

    @pollingInterval.setter
    def pollingInterval(self, value: int):
        self.__pollingInterval = value
        self._property_changed('pollingInterval')        

    @property
    def grouped(self) -> bool:
        """Set to true to return results grouped by a given context (set of dimensions)."""
        return self.__grouped

    @grouped.setter
    def grouped(self, value: bool):
        self.__grouped = value
        self._property_changed('grouped')        

    @property
    def fields(self) -> Tuple[Union[dict, str], ...]:
        """Fields to be returned."""
        return self.__fields

    @fields.setter
    def fields(self, value: Tuple[Union[dict, str], ...]):
        self.__fields = value
        self._property_changed('fields')        


class DataSetFilters(Base):
        
    """Filters to restrict the set of data returned."""
       
    def __init__(self, entityFilter: EntityFilter = None, rowFilters: Tuple[DataFilter, ...] = None, advancedFilters: Tuple[AdvancedFilter, ...] = None, historyFilter: HistoryFilter = None):
        super().__init__()
        self.__entityFilter = entityFilter
        self.__rowFilters = rowFilters
        self.__advancedFilters = advancedFilters
        self.__historyFilter = historyFilter

    @property
    def entityFilter(self) -> EntityFilter:
        """Filter on entities."""
        return self.__entityFilter

    @entityFilter.setter
    def entityFilter(self, value: EntityFilter):
        self.__entityFilter = value
        self._property_changed('entityFilter')        

    @property
    def rowFilters(self) -> Tuple[DataFilter, ...]:
        """Filters on database rows."""
        return self.__rowFilters

    @rowFilters.setter
    def rowFilters(self, value: Tuple[DataFilter, ...]):
        self.__rowFilters = value
        self._property_changed('rowFilters')        

    @property
    def advancedFilters(self) -> Tuple[AdvancedFilter, ...]:
        """Advanced filter for numeric fields."""
        return self.__advancedFilters

    @advancedFilters.setter
    def advancedFilters(self, value: Tuple[AdvancedFilter, ...]):
        self.__advancedFilters = value
        self._property_changed('advancedFilters')        

    @property
    def historyFilter(self) -> HistoryFilter:
        """Restricts queries against dataset to an absolute or relative range."""
        return self.__historyFilter

    @historyFilter.setter
    def historyFilter(self, value: HistoryFilter):
        self.__historyFilter = value
        self._property_changed('historyFilter')        


class MDAPIDataQueryResponse(Base):
               
    def __init__(self, ):
        super().__init__()
        


class DataQueryResponse(Base):
               
    def __init__(self, type: str, requestId: str = None, errorMessage: str = None, id: str = None, dataSetId: str = None, entityType: Union[MeasureEntityType, str] = None, delay: int = None, data: Tuple[FieldValueMap, ...] = None, groups: Tuple[DataGroup, ...] = None):
        super().__init__()
        self.__requestId = requestId
        self.__type = type
        self.__errorMessage = errorMessage
        self.__id = id
        self.__dataSetId = dataSetId
        self.__entityType = entityType if isinstance(entityType, MeasureEntityType) else get_enum_value(MeasureEntityType, entityType)
        self.__delay = delay
        self.__data = data
        self.__groups = groups

    @property
    def requestId(self) -> str:
        """Marquee unique identifier"""
        return self.__requestId

    @requestId.setter
    def requestId(self, value: str):
        self.__requestId = value
        self._property_changed('requestId')        

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, value: str):
        self.__type = value
        self._property_changed('type')        

    @property
    def errorMessage(self) -> str:
        return self.__errorMessage

    @errorMessage.setter
    def errorMessage(self, value: str):
        self.__errorMessage = value
        self._property_changed('errorMessage')        

    @property
    def id(self) -> str:
        """Marquee unique identifier"""
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = value
        self._property_changed('id')        

    @property
    def dataSetId(self) -> str:
        """Unique id of dataset."""
        return self.__dataSetId

    @dataSetId.setter
    def dataSetId(self, value: str):
        self.__dataSetId = value
        self._property_changed('dataSetId')        

    @property
    def entityType(self) -> Union[MeasureEntityType, str]:
        """Entity type associated with a measure."""
        return self.__entityType

    @entityType.setter
    def entityType(self, value: Union[MeasureEntityType, str]):
        self.__entityType = value if isinstance(value, MeasureEntityType) else get_enum_value(MeasureEntityType, value)
        self._property_changed('entityType')        

    @property
    def delay(self) -> int:
        return self.__delay

    @delay.setter
    def delay(self, value: int):
        self.__delay = value
        self._property_changed('delay')        

    @property
    def data(self) -> Tuple[FieldValueMap, ...]:
        """Array of data elements from dataset"""
        return self.__data

    @data.setter
    def data(self, value: Tuple[FieldValueMap, ...]):
        self.__data = value
        self._property_changed('data')        

    @property
    def groups(self) -> Tuple[DataGroup, ...]:
        """If the data is requested in grouped mode, will return data group object"""
        return self.__groups

    @groups.setter
    def groups(self, value: Tuple[DataGroup, ...]):
        self.__groups = value
        self._property_changed('groups')        


class DataSetEntity(Base):
               
    def __init__(self, id: str, name: str, description: str, shortDescription: str, vendor: str, dataProduct: str, parameters: DataSetParameters, dimensions: DataSetDimensions, ownerId: str = None, mappings: Tuple[MarketDataMapping, ...] = None, startDate: datetime.date = None, mdapi: MDAPI = None, entitlements: Entitlements = None, entitlementExclusions: EntitlementExclusions = None, queryProcessors: ProcessorEntity = None, defaults: DataSetDefaults = None, filters: DataSetFilters = None, createdById: str = None, createdTime: datetime.datetime = None, lastUpdatedById: str = None, lastUpdatedTime: datetime.datetime = None, tags: Tuple[str, ...] = None):
        super().__init__()
        self.__ownerId = ownerId
        self.__id = id
        self.__name = name
        self.__description = description
        self.__shortDescription = shortDescription
        self.__mappings = mappings
        self.__vendor = vendor
        self.__startDate = startDate
        self.__mdapi = mdapi
        self.__dataProduct = dataProduct
        self.__entitlements = entitlements
        self.__entitlementExclusions = entitlementExclusions
        self.__queryProcessors = queryProcessors
        self.__parameters = parameters
        self.__dimensions = dimensions
        self.__defaults = defaults
        self.__filters = filters
        self.__createdById = createdById
        self.__createdTime = createdTime
        self.__lastUpdatedById = lastUpdatedById
        self.__lastUpdatedTime = lastUpdatedTime
        self.__tags = tags

    @property
    def ownerId(self) -> str:
        """Marquee unique identifier for user who owns the object."""
        return self.__ownerId

    @ownerId.setter
    def ownerId(self, value: str):
        self.__ownerId = value
        self._property_changed('ownerId')        

    @property
    def id(self) -> str:
        """Unique id of dataset."""
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = value
        self._property_changed('id')        

    @property
    def name(self) -> str:
        """Name of dataset."""
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value
        self._property_changed('name')        

    @property
    def description(self) -> str:
        """Description of dataset."""
        return self.__description

    @description.setter
    def description(self, value: str):
        self.__description = value
        self._property_changed('description')        

    @property
    def shortDescription(self) -> str:
        """Short description of dataset."""
        return self.__shortDescription

    @shortDescription.setter
    def shortDescription(self, value: str):
        self.__shortDescription = value
        self._property_changed('shortDescription')        

    @property
    def mappings(self) -> Tuple[MarketDataMapping, ...]:
        """Market data mappings."""
        return self.__mappings

    @mappings.setter
    def mappings(self, value: Tuple[MarketDataMapping, ...]):
        self.__mappings = value
        self._property_changed('mappings')        

    @property
    def vendor(self) -> str:
        return self.__vendor

    @vendor.setter
    def vendor(self, value: str):
        self.__vendor = value
        self._property_changed('vendor')        

    @property
    def startDate(self) -> datetime.date:
        """The start of this data set"""
        return self.__startDate

    @startDate.setter
    def startDate(self, value: datetime.date):
        self.__startDate = value
        self._property_changed('startDate')        

    @property
    def mdapi(self) -> MDAPI:
        """Defines MDAPI fields."""
        return self.__mdapi

    @mdapi.setter
    def mdapi(self, value: MDAPI):
        self.__mdapi = value
        self._property_changed('mdapi')        

    @property
    def dataProduct(self) -> str:
        """Product that dataset belongs to."""
        return self.__dataProduct

    @dataProduct.setter
    def dataProduct(self, value: str):
        self.__dataProduct = value
        self._property_changed('dataProduct')        

    @property
    def entitlements(self) -> Entitlements:
        """Defines the entitlements of a given resource"""
        return self.__entitlements

    @entitlements.setter
    def entitlements(self, value: Entitlements):
        self.__entitlements = value
        self._property_changed('entitlements')        

    @property
    def entitlementExclusions(self) -> EntitlementExclusions:
        """Defines the exclusion entitlements of a given resource"""
        return self.__entitlementExclusions

    @entitlementExclusions.setter
    def entitlementExclusions(self, value: EntitlementExclusions):
        self.__entitlementExclusions = value
        self._property_changed('entitlementExclusions')        

    @property
    def queryProcessors(self) -> ProcessorEntity:
        """Query processors for dataset."""
        return self.__queryProcessors

    @queryProcessors.setter
    def queryProcessors(self, value: ProcessorEntity):
        self.__queryProcessors = value
        self._property_changed('queryProcessors')        

    @property
    def parameters(self) -> DataSetParameters:
        """Dataset parameters."""
        return self.__parameters

    @parameters.setter
    def parameters(self, value: DataSetParameters):
        self.__parameters = value
        self._property_changed('parameters')        

    @property
    def dimensions(self) -> DataSetDimensions:
        """Dataset dimensions."""
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, value: DataSetDimensions):
        self.__dimensions = value
        self._property_changed('dimensions')        

    @property
    def defaults(self) -> DataSetDefaults:
        """Default settings."""
        return self.__defaults

    @defaults.setter
    def defaults(self, value: DataSetDefaults):
        self.__defaults = value
        self._property_changed('defaults')        

    @property
    def filters(self) -> DataSetFilters:
        """Filters to restrict the set of data returned."""
        return self.__filters

    @filters.setter
    def filters(self, value: DataSetFilters):
        self.__filters = value
        self._property_changed('filters')        

    @property
    def createdById(self) -> str:
        """Unique identifier of user who created the object"""
        return self.__createdById

    @createdById.setter
    def createdById(self, value: str):
        self.__createdById = value
        self._property_changed('createdById')        

    @property
    def createdTime(self) -> datetime.datetime:
        """Time created. ISO 8601 formatted string"""
        return self.__createdTime

    @createdTime.setter
    def createdTime(self, value: datetime.datetime):
        self.__createdTime = value
        self._property_changed('createdTime')        

    @property
    def lastUpdatedById(self) -> str:
        """Unique identifier of user who last updated the object"""
        return self.__lastUpdatedById

    @lastUpdatedById.setter
    def lastUpdatedById(self, value: str):
        self.__lastUpdatedById = value
        self._property_changed('lastUpdatedById')        

    @property
    def lastUpdatedTime(self) -> datetime.datetime:
        """Timestamp of when the object was last updated"""
        return self.__lastUpdatedTime

    @lastUpdatedTime.setter
    def lastUpdatedTime(self, value: datetime.datetime):
        self.__lastUpdatedTime = value
        self._property_changed('lastUpdatedTime')        

    @property
    def tags(self) -> Tuple[str, ...]:
        """Tags associated with dataset."""
        return self.__tags

    @tags.setter
    def tags(self, value: Tuple[str, ...]):
        self.__tags = value
        self._property_changed('tags')        


class MDAPIDataBatchResponse(Base):
               
    def __init__(self, requestId: str = None, responses: Tuple[MDAPIDataQueryResponse, ...] = None):
        super().__init__()
        self.__requestId = requestId
        self.__responses = responses

    @property
    def requestId(self) -> str:
        """Marquee unique identifier"""
        return self.__requestId

    @requestId.setter
    def requestId(self, value: str):
        self.__requestId = value
        self._property_changed('requestId')        

    @property
    def responses(self) -> Tuple[MDAPIDataQueryResponse, ...]:
        """MDAPI Data query responses"""
        return self.__responses

    @responses.setter
    def responses(self, value: Tuple[MDAPIDataQueryResponse, ...]):
        self.__responses = value
        self._property_changed('responses')        
