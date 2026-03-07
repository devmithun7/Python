# Finance Formulas Cheat Sheet

## Profitability
- **Revenue** = Price per unit x Quantity sold  
  Example: $5 x 100 = $500
- **Total Cost** = Fixed cost + (Variable cost per unit x Quantity)  
  Example: $200 + ($1 x 100) = $300
- **Operating Profit** = Revenue - Operating costs  
  Example: $500 - $300 = $200
- **Net Profit** = Revenue - All costs (including taxes, interest)  
  Example: $500 - ($300 + $20 + $10) = $170
- **Contribution Margin (per unit)** = Price per unit - Variable cost per unit  
  Example: $5 - $1 = $4
- **Contribution Margin (total)** = Contribution margin per unit x Quantity  
  Example: $4 x 100 = $400
- **Gross Margin %** = (Revenue - COGS) / Revenue  
  Example: ($500 - $300) / $500 = 40%
- **Operating Margin %** = Operating profit / Revenue  
  Example: $200 / $500 = 40%
- **Net Margin %** = Net profit / Revenue  
  Example: $170 / $500 = 34%

## Break-Even
- **Break-even units** = Fixed cost / Contribution margin per unit  
  Example: $200 / $4 = 50 units
- **Break-even revenue** = Fixed cost / Contribution margin %  
  Example: $200 / 40% = $500
- **Contribution margin %** = (Price - Variable cost) / Price  
  Example: ($5 - $1) / $5 = 80%

## Averages and Expectations
- **Weighted Average** = Sum(weight x value) / Sum(weights)  
  Example: (2x3 + 1x5) / (2+1) = 11/3 = 3.67
- **Expected Value** = Sum(probability x outcome)  
  Example: (0.6x10) + (0.4x0) = 6

## Demand and Elasticity
- **Price Elasticity of Demand** = (% change in quantity) / (% change in price)  
  Example: -20% / +10% = -2.0
- **% change** = (New - Old) / Old  
  Example: (90 - 100) / 100 = -10%

## Time Value of Money
- **Simple Interest** = Principal x Rate x Time  
  Example: $1,000 x 5% x 2 = $100
- **Compound Interest (future value)** = Principal x (1 + Rate)^Time  
  Example: $1,000 x 1.05^2 = $1,102.50
- **Present Value (PV)** = Future value / (1 + Rate)^Time  
  Example: $1,102.50 / 1.05^2 = $1,000
- **Future Value (FV)** = Present value x (1 + Rate)^Time  
  Example: $1,000 x 1.05^3 = $1,157.63
- **Annuity PV** = Payment x [1 - (1 + Rate)^(-Time)] / Rate  
  Example: $100 x [1 - 1.05^-3] / 0.05 = $272.32
- **Annuity FV** = Payment x [(1 + Rate)^Time - 1] / Rate  
  Example: $100 x (1.05^3 - 1) / 0.05 = $315.25

## Investment Returns
- **ROI** = (Gain - Cost) / Cost  
  Example: ($120 - $100) / $100 = 20%
- **CAGR** = (Ending value / Beginning value)^(1/Years) - 1  
  Example: (121 / 100)^(1/2) - 1 = 10%
- **Payback Period** = Initial investment / Annual cash inflow  
  Example: $1,000 / $250 = 4 years
- **NPV** = Sum(Cash flow_t / (1 + Rate)^t) - Initial investment  
  Example: ($600/1.1 + $600/1.1^2) - $1,000 = $32.23
- **IRR** = Discount rate where NPV = 0  
  Example: If NPV = 0 at 12%, IRR = 12%

## Cost of Capital
- **WACC** = (E/V x Re) + (D/V x Rd x (1 - Tax rate))  
  Example: (0.6x10%) + (0.4x6%x(1-25%)) = 8.4%
- **CAPM (Cost of equity)** = Risk-free rate + Beta x (Market return - Risk-free rate)  
  Example: 3% + 1.2x(8% - 3%) = 9%

## Liquidity and Leverage
- **Current Ratio** = Current assets / Current liabilities  
  Example: $500 / $250 = 2.0
- **Quick Ratio** = (Current assets - Inventory) / Current liabilities  
  Example: ($500 - $100) / $250 = 1.6
- **Debt-to-Equity** = Total debt / Total equity  
  Example: $300 / $200 = 1.5
- **Interest Coverage** = EBIT / Interest expense  
  Example: $200 / $40 = 5.0

## Unit Economics
- **Customer Lifetime Value (simple)** = Avg. revenue per period x Gross margin % x Avg. customer lifetime  
  Example: $50 x 60% x 24 = $720
- **CAC Payback (periods)** = Customer acquisition cost / Gross profit per period  
  Example: $300 / $15 = 20 months

## Depreciation
- **Straight-line depreciation (annual)** = (Cost - Salvage value) / Useful life  
  Example: ($10,000 - $2,000) / 4 = $2,000
- **Book value (end of year)** = Cost - Accumulated depreciation  
  Example: $10,000 - $2,000 = $8,000

## DuPont Analysis
- **ROE** = Net margin x Asset turnover x Equity multiplier  
  Example: 10% x 1.5 x 2.0 = 30%
- **Asset Turnover** = Revenue / Average assets  
  Example: $900 / $600 = 1.5
- **Equity Multiplier** = Average assets / Average equity  
  Example: $600 / $300 = 2.0

## Efficiency and Working Capital
- **Inventory Turnover** = COGS / Average inventory  
  Example: $500 / $100 = 5.0
- **Days Inventory Outstanding (DIO)** = 365 / Inventory turnover  
  Example: 365 / 5.0 = 73 days
- **Days Sales Outstanding (DSO)** = (Accounts receivable / Revenue) x 365  
  Example: ($60 / $600) x 365 = 36.5 days
- **Days Payable Outstanding (DPO)** = (Accounts payable / COGS) x 365  
  Example: ($50 / $500) x 365 = 36.5 days
- **Cash Conversion Cycle** = DIO + DSO - DPO  
  Example: 73 + 36.5 - 36.5 = 73 days

## Multi-Product Break-Even
- **Weighted contribution margin** = Sum(product mix % x contribution margin per unit)  
  Example: 70% x $4 + 30% x $2 = $3.40
- **Break-even units (weighted)** = Fixed cost / Weighted contribution margin  
  Example: $1,700 / $3.40 = 500 units (total)

## Probability and Decision Trees
- **Expected Value (multi-branch)** = Sum(probability x payoff)  
  Example: (0.3 x 100) + (0.5 x 50) + (0.2 x -20) = 51
- **Expected Monetary Value (EMV)** = Sum(probability x profit)  
  Example: (0.6 x 80) + (0.4 x -10) = 44

## Bonds and Valuation
- **Bond Price** = Sum(Coupon / (1 + r)^t) + Face value / (1 + r)^n  
  Example: 3-year, $1,000 face, 5% coupon, 6% r => $27.9 + $28.0 + $28.0 + $839.6 = $923.5
- **Dividend Discount Model (Gordon Growth)** = D1 / (r - g)  
  Example: $2 / (8% - 3%) = $40

## Variance and Sensitivity
- **Variance (absolute)** = Actual - Budget  
  Example: $110 - $100 = $10 unfavorable
- **Variance (percent)** = (Actual - Budget) / Budget  
  Example: $10 / $100 = 10%
- **Sensitivity (profit)** = Contribution margin per unit x Change in volume  
  Example: $4 x 25 = $100
