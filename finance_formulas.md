# Finance Formulas Cheat Sheet

## Profitability
- **Revenue** = Price per unit x Quantity sold  
  Definition: total sales dollars before any costs.  
  Used for: measuring top-line performance and sizing markets.  
  Example: $5 x 100 = $500
- **Total Cost** = Fixed cost + (Variable cost per unit x Quantity)  
  Definition: all production/operating costs at a given volume.  
  Used for: estimating profit and break-even volume.  
  Example: $200 + ($1 x 100) = $300
- **Operating Profit** = Revenue - Operating costs  
  Definition: profit from core operations before interest/taxes.  
  Used for: assessing operating efficiency.  
  Example: $500 - $300 = $200
- **Net Profit** = Revenue - All costs (including taxes, interest)  
  Definition: bottom-line profit after all expenses.  
  Used for: overall profitability and shareholder returns.  
  Example: $500 - ($300 + $20 + $10) = $170
- **Contribution Margin (per unit)** = Price per unit - Variable cost per unit  
  Definition: profit per unit before fixed costs.  
  Used for: break-even and pricing decisions.  
  Example: $5 - $1 = $4
- **Contribution Margin (total)** = Contribution margin per unit x Quantity  
  Definition: total contribution toward fixed costs and profit.  
  Used for: assessing profit at a given volume.  
  Example: $4 x 100 = $400
- **Gross Margin %** = (Revenue - COGS) / Revenue  
  Definition: percent of sales left after direct costs.  
  Used for: product-level profitability and benchmarking.  
  Example: ($500 - $300) / $500 = 40%
- **Operating Margin %** = Operating profit / Revenue  
  Definition: percent of sales left after operating costs.  
  Used for: comparing operational efficiency across firms.  
  Example: $200 / $500 = 40%
- **Net Margin %** = Net profit / Revenue  
  Definition: percent of sales kept as net profit.  
  Used for: comparing overall profitability.  
  Example: $170 / $500 = 34%

## Break-Even
- **Break-even units** = Fixed cost / Contribution margin per unit  
  Definition: units needed to cover all fixed costs.  
  Used for: volume targets and feasibility checks.  
  Example: $200 / $4 = 50 units
- **Break-even revenue** = Fixed cost / Contribution margin %  
  Definition: sales dollars needed to cover fixed costs.  
  Used for: pricing/volume planning.  
  Example: $200 / 40% = $500
- **Contribution margin %** = (Price - Variable cost) / Price  
  Definition: share of each sales dollar that covers fixed costs/profit.  
  Used for: break-even and sensitivity analysis.  
  Example: ($5 - $1) / $5 = 80%

## Averages and Expectations
- **Weighted Average** = Sum(weight x value) / Sum(weights)  
  Definition: average that accounts for different sizes or importance.  
  Used for: blended rates, costs, and performance.  
  Example: (2x3 + 1x5) / (2+1) = 11/3 = 3.67
- **Expected Value** = Sum(probability x outcome)  
  Definition: probability-weighted average outcome.  
  Used for: decision-making under uncertainty.  
  Example: (0.6x10) + (0.4x0) = 6

## Demand and Elasticity
- **Price Elasticity of Demand** = (% change in quantity) / (% change in price)  
  Definition: how sensitive demand is to price changes.  
  Used for: pricing strategy and revenue impact.  
  Example: -20% / +10% = -2.0
- **% change** = (New - Old) / Old  
  Definition: relative change from a baseline.  
  Used for: growth, elasticity, and trend analysis.  
  Example: (90 - 100) / 100 = -10%

## Time Value of Money
- **Simple Interest** = Principal x Rate x Time  
  Definition: interest earned only on principal.  
  Used for: short-term or non-compounding loans.  
  Example: $1,000 x 5% x 2 = $100
- **Compound Interest (future value)** = Principal x (1 + Rate)^Time  
  Definition: interest earned on principal plus prior interest.  
  Used for: long-term growth and savings.  
  Example: $1,000 x 1.05^2 = $1,102.50
- **Present Value (PV)** = Future value / (1 + Rate)^Time  
  Definition: today’s value of a future amount.  
  Used for: valuation and investment decisions.  
  Example: $1,102.50 / 1.05^2 = $1,000
- **Future Value (FV)** = Present value x (1 + Rate)^Time  
  Definition: value of today’s money in the future.  
  Used for: savings and investment planning.  
  Example: $1,000 x 1.05^3 = $1,157.63
- **Annuity PV** = Payment x [1 - (1 + Rate)^(-Time)] / Rate  
  Definition: current value of a fixed stream of payments.  
  Used for: loan pricing and lease valuation.  
  Example: $100 x [1 - 1.05^-3] / 0.05 = $272.32
- **Annuity FV** = Payment x [(1 + Rate)^Time - 1] / Rate  
  Definition: future value of a fixed stream of payments.  
  Used for: savings plans and pensions.  
  Example: $100 x (1.05^3 - 1) / 0.05 = $315.25

## Investment Returns
- **ROI** = (Gain - Cost) / Cost  
  Definition: return relative to the amount invested.  
  Used for: comparing simple investment outcomes.  
  Example: ($120 - $100) / $100 = 20%
- **CAGR** = (Ending value / Beginning value)^(1/Years) - 1  
  Definition: average annual growth rate over time.  
  Used for: comparing investments with different horizons.  
  Example: (121 / 100)^(1/2) - 1 = 10%
- **Payback Period** = Initial investment / Annual cash inflow  
  Definition: time to recover the initial investment.  
  Used for: liquidity-focused project screening.  
  Example: $1,000 / $250 = 4 years
- **NPV** = Sum(Cash flow_t / (1 + Rate)^t) - Initial investment  
  Definition: value created after discounting cash flows.  
  Used for: deciding whether a project adds value.  
  Example: ($600/1.1 + $600/1.1^2) - $1,000 = $32.23
- **IRR** = Discount rate where NPV = 0  
  Definition: break-even discount rate for a project.  
  Used for: comparing project returns to hurdle rates.  
  Example: If NPV = 0 at 12%, IRR = 12%

## Cost of Capital
- **WACC** = (E/V x Re) + (D/V x Rd x (1 - Tax rate))  
  Definition: weighted average cost of financing.  
  Used for: discount rate in valuation models.  
  Example: (0.6x10%) + (0.4x6%x(1-25%)) = 8.4%
- **CAPM (Cost of equity)** = Risk-free rate + Beta x (Market return - Risk-free rate)  
  Definition: expected return required by equity investors.  
  Used for: estimating cost of equity for WACC.  
  Example: 3% + 1.2x(8% - 3%) = 9%

## Liquidity and Leverage
- **Current Ratio** = Current assets / Current liabilities  
  Definition: ability to cover short-term obligations.  
  Used for: assessing liquidity risk.  
  Example: $500 / $250 = 2.0
- **Quick Ratio** = (Current assets - Inventory) / Current liabilities  
  Definition: liquidity excluding less liquid inventory.  
  Used for: stricter short-term solvency check.  
  Example: ($500 - $100) / $250 = 1.6
- **Debt-to-Equity** = Total debt / Total equity  
  Definition: leverage relative to equity capital.  
  Used for: risk and capital structure analysis.  
  Example: $300 / $200 = 1.5
- **Interest Coverage** = EBIT / Interest expense  
  Definition: ability to pay interest from operating profit.  
  Used for: credit risk assessment.  
  Example: $200 / $40 = 5.0

## Unit Economics
- **Customer Lifetime Value (simple)** = Avg. revenue per period x Gross margin % x Avg. customer lifetime  
  Definition: total gross profit from a typical customer.  
  Used for: customer acquisition and retention decisions.  
  Example: $50 x 60% x 24 = $720
- **CAC Payback (periods)** = Customer acquisition cost / Gross profit per period  
  Definition: time to recover acquisition spend.  
  Used for: assessing growth efficiency.  
  Example: $300 / $15 = 20 months

## Depreciation
- **Straight-line depreciation (annual)** = (Cost - Salvage value) / Useful life  
  Definition: even allocation of asset cost over time.  
  Used for: forecasting expenses and earnings.  
  Example: ($10,000 - $2,000) / 4 = $2,000
- **Book value (end of year)** = Cost - Accumulated depreciation  
  Definition: remaining accounting value of an asset.  
  Used for: balance sheet reporting.  
  Example: $10,000 - $2,000 = $8,000

## DuPont Analysis
- **ROE** = Net margin x Asset turnover x Equity multiplier  
  Definition: return to equity decomposed into drivers.  
  Used for: diagnosing ROE improvements.  
  Example: 10% x 1.5 x 2.0 = 30%
- **Asset Turnover** = Revenue / Average assets  
  Definition: efficiency in using assets to generate sales.  
  Used for: operational efficiency comparisons.  
  Example: $900 / $600 = 1.5
- **Equity Multiplier** = Average assets / Average equity  
  Definition: leverage measure in DuPont analysis.  
  Used for: understanding balance-sheet leverage.  
  Example: $600 / $300 = 2.0

## Efficiency and Working Capital
- **Inventory Turnover** = COGS / Average inventory  
  Definition: how fast inventory is sold and replaced.  
  Used for: inventory management and cash flow.  
  Example: $500 / $100 = 5.0
- **Days Inventory Outstanding (DIO)** = 365 / Inventory turnover  
  Definition: average days inventory is held.  
  Used for: working capital optimization.  
  Example: 365 / 5.0 = 73 days
- **Days Sales Outstanding (DSO)** = (Accounts receivable / Revenue) x 365  
  Definition: average days to collect cash from customers.  
  Used for: credit policy and cash flow control.  
  Example: ($60 / $600) x 365 = 36.5 days
- **Days Payable Outstanding (DPO)** = (Accounts payable / COGS) x 365  
  Definition: average days to pay suppliers.  
  Used for: cash management and supplier terms.  
  Example: ($50 / $500) x 365 = 36.5 days
- **Cash Conversion Cycle** = DIO + DSO - DPO  
  Definition: time from cash out to cash in.  
  Used for: working capital performance.  
  Example: 73 + 36.5 - 36.5 = 73 days

## Multi-Product Break-Even
- **Weighted contribution margin** = Sum(product mix % x contribution margin per unit)  
  Definition: blended contribution per unit across products.  
  Used for: break-even in product-mix scenarios.  
  Example: 70% x $4 + 30% x $2 = $3.40
- **Break-even units (weighted)** = Fixed cost / Weighted contribution margin  
  Definition: total units needed across the mix to break even.  
  Used for: planning across multiple product lines.  
  Example: $1,700 / $3.40 = 500 units (total)

## Probability and Decision Trees
- **Expected Value (multi-branch)** = Sum(probability x payoff)  
  Definition: average payoff across several outcomes.  
  Used for: choosing among risky options.  
  Example: (0.3 x 100) + (0.5 x 50) + (0.2 x -20) = 51
- **Expected Monetary Value (EMV)** = Sum(probability x profit)  
  Definition: expected profit from a decision.  
  Used for: decision tree comparisons.  
  Example: (0.6 x 80) + (0.4 x -10) = 44

## Bonds and Valuation
- **Bond Price** = Sum(Coupon / (1 + r)^t) + Face value / (1 + r)^n  
  Definition: present value of bond cash flows.  
  Used for: bond valuation and yield analysis.  
  Example: 3-year, $1,000 face, 5% coupon, 6% r => $27.9 + $28.0 + $28.0 + $839.6 = $923.5
- **Dividend Discount Model (Gordon Growth)** = D1 / (r - g)  
  Definition: value of a stock with constant dividend growth.  
  Used for: equity valuation with stable dividends.  
  Example: $2 / (8% - 3%) = $40

## Variance and Sensitivity
- **Variance (absolute)** = Actual - Budget  
  Definition: difference between actual and planned results.  
  Used for: performance tracking and control.  
  Example: $110 - $100 = $10 unfavorable
- **Variance (percent)** = (Actual - Budget) / Budget  
  Definition: percent difference from plan.  
  Used for: scaling variances across items.  
  Example: $10 / $100 = 10%
- **Sensitivity (profit)** = Contribution margin per unit x Change in volume  
  Definition: profit impact from a volume change.  
  Used for: scenario and risk analysis.  
  Example: $4 x 25 = $100
