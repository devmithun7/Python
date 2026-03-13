# Finance Formulas Cheat Sheet

---

## 1. Profitability

### Revenue
$$\text{Revenue} = \text{Price per Unit} \times \text{Quantity Sold}$$

| Component | Definition |
|---|---|
| **Price per Unit** | The selling price of a single unit ($) |
| **Quantity Sold** | Number of units sold in the period |

**Interpretation:** Total sales dollars generated before any costs are deducted.  
**Use case:** Measuring top-line growth; sizing a product's market potential.  
**Example:**  
A SaaS company charges $120/month per seat and has 800 active seats.  
$$\text{Revenue} = \$120 \times 800 = \$96,000/\text{month}$$

---

### Total Cost
$$\text{Total Cost} = \text{Fixed Costs} + (\text{Variable Cost per Unit} \times \text{Quantity Produced})$$

| Component | Definition |
|---|---|
| **Fixed Costs** | Costs unchanged by volume (rent, salaries, insurance) |
| **Variable Cost per Unit** | Cost incurred for each additional unit (materials, commissions) |
| **Quantity Produced** | Number of units manufactured or delivered |

**Interpretation:** The sum of all costs at a specific output level.  
**Use case:** Forecasting operating expenses and identifying cost drivers.  
**Example:**  
A factory has $50,000/month in fixed costs, $8 variable cost per unit, and produces 10,000 units.  
$$\text{Total Cost} = \$50,000 + (\$8 \times 10,000) = \$130,000$$

---

### Gross Profit
$$\text{Gross Profit} = \text{Revenue} - \text{Cost of Goods Sold (COGS)}$$

| Component | Definition |
|---|---|
| **Revenue** | Total sales dollars |
| **COGS** | Direct costs tied to producing the goods sold (materials, direct labor) |

**Interpretation:** Profit remaining after direct production costs; before operating expenses.  
**Use case:** Assessing product-level profitability.  
**Example:**  
Revenue = $96,000; COGS (server costs + direct labor) = $32,000  
$$\text{Gross Profit} = \$96,000 - \$32,000 = \$64,000$$

---

### Operating Profit (EBIT)
$$\text{Operating Profit} = \text{Revenue} - \text{Operating Costs}$$

| Component | Definition | 
|---|---|
| **Revenue** | Total sales dollars |
| **Operating Costs** | COGS + SG&A + R&D — all costs before interest and taxes |

**Interpretation:** Profit from core business operations, before financing costs and taxes.  
**Use case:** Comparing operational efficiency across companies or time periods.  
**Example:**  
Revenue = $96,000; Operating costs (COGS + salaries + marketing) = $74,000  
$$\text{Operating Profit} = \$96,000 - \$74,000 = \$22,000$$

---

### Net Profit
$$\text{Net Profit} = \text{Revenue} - \text{Total Expenses (including interest \& taxes)}$$

| Component | Definition |
|---|---|
| **Revenue** | Total sales dollars |
| **Total Expenses** | Operating costs + interest expense + income taxes |

**Interpretation:** The bottom-line profit belonging to shareholders after every obligation.  
**Use case:** Evaluating overall company profitability; basis for EPS and dividends.  
**Example:**  
Revenue = $96,000; Operating costs = $74,000; Interest = $1,500; Taxes = $4,200  
$$\text{Net Profit} = \$96,000 - (\$74,000 + \$1,500 + \$4,200) = \$16,300$$

---

### Contribution Margin per Unit
$$\text{CM per Unit} = \text{Price per Unit} - \text{Variable Cost per Unit}$$

| Component | Definition |
|---|---|
| **Price per Unit** | Revenue received for selling one unit |
| **Variable Cost per Unit** | Cost incurred to produce one additional unit |

**Interpretation:** The dollar amount each unit sold contributes toward covering fixed costs and generating profit.  
**Use case:** Pricing decisions; understanding how volume changes affect profit.  
**Example:**  
A smartphone accessory sells for $25; materials + packaging = $9/unit  
$$\text{CM per Unit} = \$25 - \$9 = \$16$$

---

### Gross Margin %
$$\text{Gross Margin \%} = \frac{\text{Revenue} - \text{COGS}}{\text{Revenue}} \times 100 = \frac{\text{Gross Profit}}{\text{Revenue}} \times 100$$

| Component | Definition |
|---|---|
| **Numerator** | Gross Profit = revenue minus direct production costs |
| **Denominator** | Revenue = total sales dollars |

**Interpretation:** What percentage of each sales dollar remains after paying for what was sold.  
**Use case:** Benchmarking product margins against competitors; tracking pricing power.  
**Example:**  
Revenue = $96,000; COGS = $32,000  
$$\text{Gross Margin \%} = \frac{\$96,000 - \$32,000}{\$96,000} = \frac{\$64,000}{\$96,000} = 66.7\%$$

---

### Operating Margin %
$$\text{Operating Margin \%} = \frac{\text{Operating Profit (EBIT)}}{\text{Revenue}} \times 100$$

| Component | Definition |
|---|---|
| **Numerator** | Operating Profit (EBIT) — profit after all operating costs |
| **Denominator** | Revenue = total sales dollars |

**Interpretation:** What percentage of each sales dollar remains after all operating costs.  
**Use case:** Comparing cost efficiency across companies regardless of financing choices.  
**Example:**  
Operating Profit = $22,000; Revenue = $96,000  
$$\text{Operating Margin \%} = \frac{\$22,000}{\$96,000} = 22.9\%$$

---

### Net Margin %
$$\text{Net Margin \%} = \frac{\text{Net Profit}}{\text{Revenue}} \times 100$$

| Component | Definition |
|---|---|
| **Numerator** | Net Profit — after all expenses, interest, and taxes |
| **Denominator** | Revenue = total sales dollars |

**Interpretation:** Percentage of each sales dollar kept as profit after every cost.  
**Use case:** Comparing overall profitability across industries or time periods.  
**Example:**  
Net Profit = $16,300; Revenue = $96,000  
$$\text{Net Margin \%} = \frac{\$16,300}{\$96,000} = 17.0\%$$

---

## 2. Break-Even Analysis

### Contribution Margin % (CM Ratio)
$$\text{CM \%} = \frac{\text{Price per Unit} - \text{Variable Cost per Unit}}{\text{Price per Unit}} \times 100 = \frac{\text{CM per Unit}}{\text{Price per Unit}} \times 100$$

| Component | Definition |
|---|---|
| **Numerator** | CM per Unit = the portion of the selling price not consumed by variable costs |
| **Denominator** | Price per Unit = full selling price |

**Interpretation:** The fraction of every sales dollar available to cover fixed costs and profit.  
**Use case:** Calculating break-even revenue; pricing sensitivity analysis.  
**Example:**  
Price = $25; Variable Cost = $9 → CM per Unit = $16  
$$\text{CM \%} = \frac{\$16}{\$25} = 64\%$$

---

### Break-Even Units
$$\text{Break-Even Units} = \frac{\text{Total Fixed Costs}}{\text{Contribution Margin per Unit}}$$

| Component | Definition |
|---|---|
| **Numerator** | Total Fixed Costs = costs that must be covered regardless of volume |
| **Denominator** | CM per Unit = profit contribution from selling one additional unit |

**Interpretation:** The exact number of units that must be sold so that total contribution equals total fixed costs (profit = $0).  
**Use case:** Setting minimum sales targets; go/no-go decisions for new products.  
**Example:**  
Fixed Costs = $80,000/month; CM per Unit = $16  
$$\text{Break-Even Units} = \frac{\$80,000}{\$16} = 5,000 \text{ units}$$

---

### Break-Even Revenue
$$\text{Break-Even Revenue} = \frac{\text{Total Fixed Costs}}{\text{Contribution Margin \%}}$$

| Component | Definition |
|---|---|
| **Numerator** | Total Fixed Costs = the dollar amount of overhead to be covered |
| **Denominator** | CM % = fraction of each revenue dollar that contributes to covering fixed costs |

**Interpretation:** The total sales dollars required to cover all fixed costs with zero profit remaining.  
**Use case:** Revenue planning and scenario analysis when unit prices vary.  
**Example:**  
Fixed Costs = $80,000; CM % = 64%  
$$\text{Break-Even Revenue} = \frac{\$80,000}{0.64} = \$125,000$$

---

## 3. Averages and Expectations

### Weighted Average
$$\text{Weighted Average} = \frac{\displaystyle\sum_{i}(w_i \times x_i)}{\displaystyle\sum_{i} w_i}$$

| Component | Definition |
|---|---|
| **Numerator** | Sum of each value multiplied by its weight |
| **Denominator** | Sum of all weights |
| **$w_i$** | Weight of item $i$ (size, importance, or proportion) |
| **$x_i$** | Value of item $i$ |

**Interpretation:** An average that accounts for the relative size or importance of each observation — larger weights pull the result closer to their value.  
**Use case:** Calculating a blended interest rate across loans of different sizes; portfolio return.  
**Example:**  
A company has two loans: $200K at 5% and $800K at 8%.  
$$\text{Weighted Avg Rate} = \frac{(200{,}000 \times 5\%) + (800{,}000 \times 8\%)}{200{,}000 + 800{,}000} = \frac{10{,}000 + 64{,}000}{1{,}000{,}000} = 7.4\%$$

---

### Expected Value (EV)
$$\text{EV} = \sum_{i} p_i \times x_i$$

| Component | Definition |
|---|---|
| **$p_i$** | Probability of outcome $i$ (all probabilities must sum to 1) |
| **$x_i$** | Payoff or value of outcome $i$ |

**Interpretation:** The probability-weighted average outcome across all scenarios.  
**Use case:** Deciding between business options when outcomes are uncertain.  
**Example:**  
A new product launch has three scenarios:

| Scenario | Probability | Profit |
|---|---|---|
| Strong market | 40% | +$500K |
| Moderate market | 45% | +$150K |
| Weak market | 15% | −$200K |

$$\text{EV} = (0.40 \times 500) + (0.45 \times 150) + (0.15 \times -200) = 200 + 67.5 - 30 = \$237.5\text{K}$$

---

## 4. Demand and Elasticity

### % Change
$$\% \text{ Change} = \frac{\text{New Value} - \text{Old Value}}{\text{Old Value}} \times 100$$

| Component | Definition |
|---|---|
| **Numerator** | New Value − Old Value = the absolute change |
| **Denominator** | Old Value = the baseline or starting point |

**Interpretation:** Relative change expressed as a percentage of the starting value.  
**Use case:** Calculating revenue growth, price changes, or volume shifts.  
**Example:**  
Units sold went from 4,000 to 4,600.  
$$\% \text{ Change} = \frac{4{,}600 - 4{,}000}{4{,}000} = \frac{600}{4{,}000} = +15\%$$

---

### Price Elasticity of Demand (PED)
$$\text{PED} = \frac{\% \text{ Change in Quantity Demanded}}{\% \text{ Change in Price}}$$

| Component | Definition |
|---|---|
| **Numerator** | % change in quantity demanded — how much demand shifted |
| **Denominator** | % change in price — what caused the demand shift |

**Interpretation:**
- $|\text{PED}| > 1$ → **Elastic** — demand is sensitive to price; raising price *reduces* total revenue
- $|\text{PED}| < 1$ → **Inelastic** — demand is insensitive to price; raising price *increases* total revenue
- The result is normally negative (price up → demand down)

**Use case:** Setting prices to maximize revenue; predicting volume impact of price changes.  
**Example:**  
Price raised from $10 → $11 (+10%). Demand fell from 1,000 → 850 units (−15%).  
$$\text{PED} = \frac{-15\%}{+10\%} = -1.5 \quad \Rightarrow \text{Elastic — raising price reduces total revenue}$$

---

## 5. Time Value of Money

### Simple Interest
$$\text{Interest} = P \times r \times t$$

| Component | Definition |
|---|---|
| **$P$** | Principal — the original amount borrowed or invested |
| **$r$** | Annual interest rate (as a decimal, e.g., 6% = 0.06) |
| **$t$** | Time in years |

**Interpretation:** Interest earned only on the original principal; no compounding.  
**Use case:** Short-term loans, trade credit, or simple savings instruments.  
**Example:**  
A $5,000 short-term loan at 6% per year for 9 months ($t = 0.75$).  
$$\text{Interest} = \$5,000 \times 0.06 \times 0.75 = \$225$$

---

### Compound Interest — Future Value
$$\text{FV} = P \times (1 + r)^t$$

| Component | Definition |
|---|---|
| **$P$** | Principal — initial amount |
| **$r$** | Annual interest rate (decimal) |
| **$t$** | Number of compounding periods (years) |

**Interpretation:** The value your money grows to when interest is earned on both the principal and all previously accumulated interest.  
**Use case:** Projecting investment or savings account balances over time.  
**Example:**  
$10,000 invested at 7% per year for 5 years.  
$$\text{FV} = \$10,000 \times (1.07)^5 = \$10,000 \times 1.4026 = \$14,026$$

---

### Present Value (PV)
$$\text{PV} = \frac{\text{Future Value}}{(1 + r)^t}$$

| Component | Definition |
|---|---|
| **Numerator** | Future Value — the cash amount expected to be received |
| **Denominator** | $(1 + r)^t$ — discount factor; how much $1 today grows to in $t$ years at rate $r$ |
| **$r$** | Discount rate (opportunity cost of capital) |
| **$t$** | Number of years until the cash is received |

**Interpretation:** What a future cash amount is worth in today's dollars — accounts for the fact that money available now is more valuable than money received later.  
**Use case:** Valuing a future payment; comparing investment options on a like-for-like basis.  
**Example:**  
You will receive $14,026 in 5 years. Your discount rate is 7%.  
$$\text{PV} = \frac{\$14,026}{(1.07)^5} = \frac{\$14,026}{1.4026} = \$10,000$$

---

### Future Value (FV)
$$\text{FV} = \text{PV} \times (1 + r)^t$$

*(Same mechanics as Compound Interest — see above.)*  
**Use case:** Planning how much a current savings balance will grow to at a future date.  
**Example:**  
You invest $20,000 today at 8% for 10 years.  
$$\text{FV} = \$20,000 \times (1.08)^{10} = \$20,000 \times 2.1589 = \$43,178$$

---

### Annuity — Present Value
$$\text{Annuity PV} = \text{PMT} \times \frac{1 - (1 + r)^{-n}}{r}$$

| Component | Definition |
|---|---|
| **PMT** | Fixed payment amount per period |
| **Numerator** | $1 - (1+r)^{-n}$ — total discount factor across all $n$ periods |
| **Denominator** | $r$ — the periodic discount rate |
| **$n$** | Number of periods |

**Interpretation:** The lump-sum value today of a fixed stream of future payments.  
**Use case:** Pricing a loan, valuing a lease, determining how much a pension is worth today.  
**Example:**  
A 5-year lease pays $12,000/year. Discount rate = 8%.  
$$\text{Annuity PV} = \$12,000 \times \frac{1 - (1.08)^{-5}}{0.08} = \$12,000 \times \frac{1 - 0.6806}{0.08} = \$12,000 \times 3.993 = \$47,916$$

---

### Annuity — Future Value
$$\text{Annuity FV} = \text{PMT} \times \frac{(1 + r)^n - 1}{r}$$

| Component | Definition |
|---|---|
| **PMT** | Fixed payment amount per period |
| **Numerator** | $(1+r)^n - 1$ — total compound growth accumulated above the payments |
| **Denominator** | $r$ — the periodic interest rate |
| **$n$** | Number of periods |

**Interpretation:** The total value accumulated at the end of the period if you make equal payments each period and they earn compound interest.  
**Use case:** Calculating the balance of a savings plan or pension fund at maturity.  
**Example:**  
You save $500/month for 10 years at 6% annual rate → 0.5%/month, $n = 120$ months.  
$$\text{Annuity FV} = \$500 \times \frac{(1.005)^{120} - 1}{0.005} = \$500 \times \frac{0.8194}{0.005} = \$500 \times 163.88 = \$81,940$$

---

## 6. Investment Returns

### Return on Investment (ROI)
$$\text{ROI} = \frac{\text{Final Value} - \text{Initial Investment}}{\text{Initial Investment}} \times 100$$

| Component | Definition |
|---|---|
| **Numerator** | Net Gain = final value minus what you originally paid |
| **Denominator** | Initial Investment = the total upfront capital outlay |

**Interpretation:** The percentage return earned relative to what was invested.  
**Use case:** Quickly comparing two investments or marketing campaigns on a common scale.  
**Example:**  
You spend $8,000 on a marketing campaign. It generates $11,200 in attributable revenue.  
$$\text{ROI} = \frac{\$11,200 - \$8,000}{\$8,000} = \frac{\$3,200}{\$8,000} = 40\%$$

---

### Compound Annual Growth Rate (CAGR)
$$\text{CAGR} = \left(\frac{\text{Ending Value}}{\text{Beginning Value}}\right)^{\frac{1}{n}} - 1$$

| Component | Definition |
|---|---|
| **Numerator** | Ending Value — value at the end of the period |
| **Denominator** | Beginning Value — value at the start of the period |
| **Exponent $\frac{1}{n}$** | Converts total growth into a per-year rate over $n$ years |

**Interpretation:** The constant annual growth rate that would take the beginning value to the ending value over $n$ years — smooths out year-to-year volatility.  
**Use case:** Comparing investments or business metrics (revenue, users) that span different time horizons.  
**Example:**  
A company's revenue grew from $2.0M to $3.5M over 4 years.  
$$\text{CAGR} = \left(\frac{3.5}{2.0}\right)^{1/4} - 1 = (1.75)^{0.25} - 1 = 1.1501 - 1 = 15.0\%$$

---

### Payback Period
$$\text{Payback Period} = \frac{\text{Initial Investment}}{\text{Annual Net Cash Inflow}}$$

| Component | Definition |
|---|---|
| **Numerator** | Initial Investment = total upfront capital outlay |
| **Denominator** | Annual Net Cash Inflow = net cash generated per year from the investment |

**Interpretation:** The number of years required to recover the initial investment through operating cash flows.  
**Use case:** Quick liquidity screening — preferred when capital recovery speed matters more than total return.  
**Example:**  
A machine costs $120,000 and generates $30,000 net cash/year.  
$$\text{Payback Period} = \frac{\$120,000}{\$30,000} = 4.0 \text{ years}$$

---

### Net Present Value (NPV)
$$\text{NPV} = \sum_{t=1}^{n} \frac{\text{Cash Flow}_t}{(1 + r)^t} \;-\; \text{Initial Investment}$$

| Component | Definition |
|---|---|
| **Numerator** | Cash Flow$_t$ = net cash inflow in year $t$ |
| **Denominator** | $(1+r)^t$ — the discount factor for year $t$ |
| **$r$** | Discount rate (cost of capital / hurdle rate) |
| **Initial Investment** | Upfront cost at time 0 (subtracted because it is a cash outflow) |

**Interpretation:**
- **NPV > 0** → The project creates value; accept.
- **NPV < 0** → The project destroys value; reject.
- **NPV = 0** → The project exactly meets the required return.

**Use case:** Capital budgeting — deciding whether a project, acquisition, or expansion is financially worthwhile.  
**Example:**  
A $100,000 machine generates $45,000/year for 3 years. Discount rate = 10%.

| Year | Cash Flow | Discount Factor | PV of Cash Flow |
|------|-----------|-----------------|-----------------|
| 1 | $45,000 | ÷ 1.10¹ = 1.100 | $40,909 |
| 2 | $45,000 | ÷ 1.10² = 1.210 | $37,190 |
| 3 | $45,000 | ÷ 1.10³ = 1.331 | $33,809 |
| | | **Sum of PVs** | **$111,908** |

$$\text{NPV} = \$111,908 - \$100,000 = +\$11,908 \quad \Rightarrow \text{Accept the project}$$

---

### Internal Rate of Return (IRR)
$$\text{IRR is the rate } r \text{ such that:} \quad \sum_{t=1}^{n} \frac{\text{Cash Flow}_t}{(1 + r)^t} - \text{Initial Investment} = 0$$

**Interpretation:** The annualized return the project generates — the discount rate that makes NPV exactly zero.  
**Decision rule:** Accept if **IRR > Hurdle Rate** (cost of capital).  
**Use case:** Ranking competing projects; comparing project return against the cost of borrowing.  
**Example (same project as NPV above):**  
Initial Investment = $100,000; Cash flows = $45,000/year × 3 years.  
Solving iteratively: NPV = 0 at **r ≈ 16.7%**.  
Hurdle rate = 10% → IRR (16.7%) > Hurdle Rate → **Accept the project.**

---

## 7. Cost of Capital

### Weighted Average Cost of Capital (WACC)
$$\text{WACC} = \left(\frac{E}{V} \times R_e\right) + \left(\frac{D}{V} \times R_d \times (1 - T)\right)$$

| Component | Definition |
|---|---|
| **$E$** | Market value of equity |
| **$D$** | Market value of debt |
| **$V = E + D$** | Total firm value |
| **$E/V$** | Equity weight — fraction of financing from equity |
| **$D/V$** | Debt weight — fraction of financing from debt |
| **$R_e$** | Cost of equity (return required by shareholders) |
| **$R_d$** | Pre-tax cost of debt (interest rate on borrowing) |
| **$T$** | Corporate tax rate (interest is tax-deductible, so after-tax debt cost = $R_d \times (1-T)$) |

**Interpretation:** The blended minimum return the company must earn on its assets to satisfy all investors (both debt and equity holders).  
**Use case:** Discount rate for NPV/DCF valuations; hurdle rate for capital budgeting.  
**Example:**  
Capital structure: 70% equity at 12% cost; 30% debt at 6% pre-tax; tax rate = 25%.  
$$\text{WACC} = (0.70 \times 12\%) + (0.30 \times 6\% \times 0.75) = 8.40\% + 1.35\% = 9.75\%$$

---

### CAPM — Cost of Equity
$$R_e = R_f + \beta \times (R_m - R_f)$$

| Component | Definition |
|---|---|
| **$R_f$** | Risk-free rate (e.g., 10-year government bond yield) |
| **$\beta$** | Beta — the stock's sensitivity to market movements ($\beta = 1$ moves with the market; $\beta > 1$ is more volatile) |
| **$R_m$** | Expected market return (e.g., long-run S&P 500 average ≈ 10%) |
| **$(R_m - R_f)$** | Market risk premium — extra return demanded for bearing market risk |

**Interpretation:** The return equity investors require, compensating them for the risk-free rate plus a premium proportional to how volatile the stock is relative to the broader market.  
**Use case:** Estimating cost of equity for WACC; valuing equities in DCF models.  
**Example:**  
Risk-free rate = 4%; Expected market return = 10%; Beta = 1.3  
$$R_e = 4\% + 1.3 \times (10\% - 4\%) = 4\% + 7.8\% = 11.8\%$$

---

## 8. Liquidity and Leverage

### Current Ratio
$$\text{Current Ratio} = \frac{\text{Current Assets}}{\text{Current Liabilities}}$$

| Component | Definition |
|---|---|
| **Numerator** | Current Assets — cash, receivables, inventory; assets convertible to cash within 12 months |
| **Denominator** | Current Liabilities — obligations due within 12 months |

**Interpretation:**
- **> 1.0** → Short-term assets exceed short-term obligations (liquid)
- **< 1.0** → Potential liquidity problem

**Use case:** Lender covenant checks; quick assessment of short-term financial health.  
**Example:**  
Current Assets = $850,000 (cash $300K + receivables $250K + inventory $300K); Current Liabilities = $400,000  
$$\text{Current Ratio} = \frac{\$850,000}{\$400,000} = 2.1$$

---

### Quick Ratio (Acid-Test)
$$\text{Quick Ratio} = \frac{\text{Current Assets} - \text{Inventory}}{\text{Current Liabilities}}$$

| Component | Definition |
|---|---|
| **Numerator** | Current Assets minus Inventory — excludes the least liquid current asset |
| **Denominator** | Current Liabilities — obligations due within 12 months |

**Interpretation:** A stricter liquidity test — can the company meet near-term obligations without relying on selling inventory?  
**Use case:** Assessing liquidity in industries where inventory is slow to convert to cash (manufacturing, retail).  
**Example:**  
Using same data: Current Assets = $850,000; Inventory = $300,000; Current Liabilities = $400,000  
$$\text{Quick Ratio} = \frac{\$850,000 - \$300,000}{\$400,000} = \frac{\$550,000}{\$400,000} = 1.4$$

---

### Debt-to-Equity Ratio (D/E)
$$\text{D/E} = \frac{\text{Total Debt}}{\text{Total Shareholders' Equity}}$$

| Component | Definition |
|---|---|
| **Numerator** | Total Debt = all interest-bearing liabilities (short-term + long-term) |
| **Denominator** | Total Shareholders' Equity = total assets minus total liabilities |

**Interpretation:** How many dollars of debt exist for every dollar of equity. Higher = more financial leverage and risk.  
**Use case:** Credit analysis; evaluating capital structure risk; comparing leverage across peers.  
**Example:**  
Total Debt = $1,200,000 (bank loans + bonds); Equity = $800,000  
$$\text{D/E} = \frac{\$1,200,000}{\$800,000} = 1.5 \quad \Rightarrow \text{There is \$1.50 of debt for every \$1 of equity}$$

---

### Interest Coverage Ratio
$$\text{Interest Coverage} = \frac{\text{EBIT}}{\text{Interest Expense}}$$

| Component | Definition |
|---|---|
| **Numerator** | EBIT = Earnings Before Interest and Taxes (operating profit) |
| **Denominator** | Interest Expense = annual interest owed on all outstanding debt |

**Interpretation:** How many times over the company can pay its interest bill from operating profit.
- **> 3×** is generally considered safe
- **< 1.5×** is a warning sign

**Use case:** Bond analysis; credit risk assessment; covenant monitoring.  
**Example:**  
EBIT = $500,000; Annual interest expense = $80,000  
$$\text{Interest Coverage} = \frac{\$500,000}{\$80,000} = 6.25\times \quad \Rightarrow \text{Operating profit covers interest 6.25 times}$$

---

## 9. Unit Economics

### Customer Lifetime Value (CLV)
$$\text{CLV} = \text{Avg. Revenue per Period} \times \text{Gross Margin \%} \times \text{Avg. Customer Lifetime (periods)}$$

| Component | Definition |
|---|---|
| **Avg. Revenue per Period** | Average monthly (or annual) revenue from one customer |
| **Gross Margin %** | Fraction of revenue remaining after variable delivery costs |
| **Avg. Customer Lifetime** | Expected number of periods before the customer churns |

**Interpretation:** The total gross profit a typical customer generates over their entire relationship with the company.  
**Use case:** Setting maximum allowable customer acquisition cost (CAC); justifying retention spend.  
**Example:**  
A subscription app earns $15/month per user; gross margin = 75%; average customer stays 28 months.  
$$\text{CLV} = \$15 \times 75\% \times 28 = \$315$$

---

### CAC Payback Period
$$\text{CAC Payback} = \frac{\text{Customer Acquisition Cost (CAC)}}{\text{Gross Profit per Period per Customer}}$$

| Component | Definition |
|---|---|
| **Numerator** | CAC = total sales & marketing spend ÷ number of new customers acquired |
| **Denominator** | Gross Profit per Period = Revenue per customer × Gross Margin % |

**Interpretation:** How many periods it takes to recover the cost of acquiring one customer from the gross profit that customer generates.  
**Use case:** Assessing growth efficiency; ensuring acquisition cost is justified by lifetime value.  
**Example:**  
CAC = $180; Monthly gross profit per customer = $15 × 75% = $11.25  
$$\text{CAC Payback} = \frac{\$180}{\$11.25} = 16 \text{ months}$$
Sanity check: CLV ($315) >> CAC ($180) → healthy unit economics.

---

## 10. Depreciation

### Straight-Line Depreciation (Annual)
$$\text{Annual Depreciation} = \frac{\text{Cost} - \text{Salvage Value}}{\text{Useful Life (years)}}$$

| Component | Definition |
|---|---|
| **Numerator** | Cost − Salvage Value = the total amount to be depreciated (the "depreciable base") |
| **Denominator** | Useful Life = how many years the asset is expected to be used |
| **Salvage Value** | Estimated resale or scrap value at the end of the asset's useful life |

**Interpretation:** Allocates the depreciable cost evenly across each year of the asset's useful life.  
**Use case:** Forecasting D&A expense on the income statement; calculating EBITDA.  
**Example:**  
A delivery van costs $48,000, has a salvage value of $6,000, and a useful life of 6 years.  
$$\text{Annual Depreciation} = \frac{\$48,000 - \$6,000}{6} = \frac{\$42,000}{6} = \$7,000/\text{year}$$

---

### Book Value (Net of Depreciation)
$$\text{Book Value} = \text{Original Cost} - \text{Accumulated Depreciation}$$

| Component | Definition |
|---|---|
| **Original Cost** | Purchase price of the asset |
| **Accumulated Depreciation** | Total depreciation charged since purchase = Annual Depreciation × years elapsed |

**Interpretation:** The remaining accounting value of the asset carried on the balance sheet.  
**Use case:** Balance sheet reporting; calculating gain or loss on asset disposal.  
**Example:**  
After 3 years: Accumulated Depreciation = $7,000 × 3 = $21,000  
$$\text{Book Value} = \$48,000 - \$21,000 = \$27,000$$

---

## 11. DuPont Analysis

### Return on Equity (ROE) — DuPont Decomposition
$$\text{ROE} = \underbrace{\frac{\text{Net Profit}}{\text{Revenue}}}_{\text{Net Margin}} \;\times\; \underbrace{\frac{\text{Revenue}}{\text{Avg. Total Assets}}}_{\text{Asset Turnover}} \;\times\; \underbrace{\frac{\text{Avg. Total Assets}}{\text{Avg. Shareholders' Equity}}}_{\text{Equity Multiplier}}$$

| Driver | What it measures | How to improve |
|---|---|---|
| **Net Margin** | Profitability — profit kept per sales dollar | Cut costs or raise prices |
| **Asset Turnover** | Efficiency — sales generated per dollar of assets | Increase revenue or reduce assets |
| **Equity Multiplier** | Leverage — assets funded per dollar of equity | Take on more debt (increases risk) |

**Interpretation:** Decomposes ROE into three levers so management can diagnose *why* ROE is high or low.  
**Use case:** Identifying whether ROE improvements come from better margins, better asset use, or higher leverage.  
**Example:**  
Net Margin = 8%; Asset Turnover = 1.6×; Equity Multiplier = 2.5×  
$$\text{ROE} = 8\% \times 1.6 \times 2.5 = 32\%$$
The high ROE is partly driven by leverage (2.5×); reducing leverage to 1.5× would drop ROE to 19.2%.

---

### Asset Turnover
$$\text{Asset Turnover} = \frac{\text{Revenue}}{\text{Average Total Assets}}$$

| Component | Definition |
|---|---|
| **Numerator** | Revenue = total annual sales |
| **Denominator** | Average Total Assets = (Opening assets + Closing assets) ÷ 2 |

**Interpretation:** How many dollars of revenue are generated for every dollar of assets held.  
**Example:**  
Revenue = $4.8M; Beginning assets = $2.8M; Ending assets = $3.2M → Average = $3.0M  
$$\text{Asset Turnover} = \frac{\$4.8M}{\$3.0M} = 1.6\times$$

---

### Equity Multiplier
$$\text{Equity Multiplier} = \frac{\text{Average Total Assets}}{\text{Average Shareholders' Equity}}$$

| Component | Definition |
|---|---|
| **Numerator** | Average Total Assets = total assets the business controls |
| **Denominator** | Average Shareholders' Equity = net assets funded by owners |

**Interpretation:** How many dollars of assets exist per dollar of equity — measures balance-sheet leverage.  
**Example:**  
Avg Total Assets = $3.0M; Avg Equity = $1.2M  
$$\text{Equity Multiplier} = \frac{\$3.0M}{\$1.2M} = 2.5\times$$

---

## 12. Efficiency and Working Capital

### Inventory Turnover
$$\text{Inventory Turnover} = \frac{\text{Cost of Goods Sold (COGS)}}{\text{Average Inventory}}$$

| Component | Definition |
|---|---|
| **Numerator** | COGS = cost of inventory actually sold during the period |
| **Denominator** | Average Inventory = (Opening inventory + Closing inventory) ÷ 2 |

**Interpretation:** How many times inventory is fully sold and replaced during the year. Higher = leaner operations.  
**Use case:** Identifying slow-moving stock; comparing supply chain efficiency with peers.  
**Example:**  
Annual COGS = $1,800,000; Beginning inventory = $300,000; Ending inventory = $420,000 → Average = $360,000  
$$\text{Inventory Turnover} = \frac{\$1,800,000}{\$360,000} = 5.0\times$$

---

### Days Inventory Outstanding (DIO)
$$\text{DIO} = \frac{365}{\text{Inventory Turnover}}$$

| Component | Definition |
|---|---|
| **Numerator** | 365 — days in a year |
| **Denominator** | Inventory Turnover — how many full cycles occur per year |

**Interpretation:** The average number of days inventory sits on the shelf before being sold.  
**Use case:** Working capital optimization; identifying excess or obsolete stock.  
**Example:**  
$$\text{DIO} = \frac{365}{5.0} = 73 \text{ days}$$

---

### Days Sales Outstanding (DSO)
$$\text{DSO} = \frac{\text{Accounts Receivable}}{\text{Annual Revenue}} \times 365$$

| Component | Definition |
|---|---|
| **Numerator** | Accounts Receivable = money owed by customers at period end |
| **Denominator** | Annual Revenue ÷ 365 = average daily revenue (dividing AR by this gives days outstanding) |

**Interpretation:** The average number of days it takes to collect cash after making a sale.  
**Use case:** Managing credit policy; identifying collection problems; cash flow forecasting.  
**Example:**  
Accounts Receivable = $180,000; Annual Revenue = $1,800,000  
$$\text{DSO} = \frac{\$180,000}{\$1,800,000} \times 365 = 0.10 \times 365 = 36.5 \text{ days}$$

---

### Days Payable Outstanding (DPO)
$$\text{DPO} = \frac{\text{Accounts Payable}}{\text{COGS}} \times 365$$

| Component | Definition |
|---|---|
| **Numerator** | Accounts Payable = money owed to suppliers at period end |
| **Denominator** | COGS ÷ 365 = average daily purchases from suppliers |

**Interpretation:** The average number of days the company takes to pay its suppliers. Higher DPO = company holds cash longer (favorable for liquidity).  
**Use case:** Supplier negotiation; cash management strategy.  
**Example:**  
Accounts Payable = $180,000; Annual COGS = $1,800,000  
$$\text{DPO} = \frac{\$180,000}{\$1,800,000} \times 365 = 36.5 \text{ days}$$

---

### Cash Conversion Cycle (CCC)
$$\text{CCC} = \text{DIO} + \text{DSO} - \text{DPO}$$

| Component | Definition |
|---|---|
| **DIO** | Days inventory is held before being sold |
| **DSO** | Days to collect cash from customers after the sale |
| **DPO** | Days taken to pay suppliers — *subtracted* because it delays the cash outflow |

**Interpretation:** The number of days cash is tied up in operations from the moment you pay for inventory to the moment you collect from customers. **Lower CCC = better cash efficiency.**  
**Use case:** Working capital management; identifying cash flow bottlenecks.  
**Example:**  
DIO = 73 days; DSO = 36.5 days; DPO = 36.5 days  
$$\text{CCC} = 73 + 36.5 - 36.5 = 73 \text{ days}$$
To improve: negotiate supplier terms to extend DPO to 50 days → CCC drops to 59.5 days.

---

## 13. Multi-Product Break-Even

### Weighted Contribution Margin
$$\text{Weighted CM} = \sum_{i}\left(\text{Product Mix \%}_i \times \text{CM per Unit}_i\right)$$

| Component | Definition |
|---|---|
| **Product Mix %** | Share of total unit sales each product represents (all must sum to 100%) |
| **CM per Unit** | Contribution margin of each individual product |

**Interpretation:** The average contribution per unit sold across the entire product portfolio, weighted by sales mix.  
**Use case:** Break-even analysis when a company sells more than one product.  
**Example:**  
Product A: 60% of sales, CM = $20/unit. Product B: 40% of sales, CM = $8/unit.  
$$\text{Weighted CM} = (0.60 \times \$20) + (0.40 \times \$8) = \$12.00 + \$3.20 = \$15.20$$

---

### Break-Even Units (Multi-Product)
$$\text{Break-Even Units (total)} = \frac{\text{Total Fixed Costs}}{\text{Weighted CM per Unit}}$$

| Component | Definition |
|---|---|
| **Numerator** | Total Fixed Costs = overhead that must be covered |
| **Denominator** | Weighted CM per Unit = blended average contribution across the product mix |

**Use case:** Planning total output required across a product portfolio to reach break-even.  
**Example:**  
Fixed Costs = $76,000; Weighted CM = $15.20  
$$\text{Break-Even Units (total)} = \frac{\$76,000}{\$15.20} = 5,000 \text{ units}$$
Split by mix: 5,000 × 60% = **3,000 units of A**; 5,000 × 40% = **2,000 units of B**.

---

## 14. Bonds and Valuation

### Bond Price
$$\text{Bond Price} = \sum_{t=1}^{n} \frac{\text{Coupon Payment}}{(1 + r)^t} + \frac{\text{Face Value}}{(1 + r)^n}$$

| Component | Definition |
|---|---|
| **Coupon Payment** | Fixed periodic cash interest = Face Value × Coupon Rate |
| **Face Value** | Par value of the bond, repaid in full at maturity (typically $1,000) |
| **Numerator (coupons)** | The cash interest received each period |
| **Numerator (final term)** | The face value received at maturity |
| **Denominator** | $(1 + r)^t$ — discount factor for each period using market yield $r$ |
| **$n$** | Total number of periods until maturity |

**Interpretation:** A bond's price equals the present value of all future cash flows discounted at the market yield.
- Market yield **rises** → Bond price **falls** (inverse relationship)
- Market yield **falls** → Bond price **rises**

**Use case:** Valuing bonds; understanding the price-yield relationship.  
**Example:**  
3-year bond; Face = $1,000; Coupon = 5% ($50/year); Market yield = 7%

| Year | Cash Flow | Discount Factor | PV of Cash Flow |
|------|-----------|-----------------|-----------------|
| 1 | $50 | ÷ 1.07¹ = 1.070 | $46.73 |
| 2 | $50 | ÷ 1.07² = 1.145 | $43.67 |
| 3 | $1,050 | ÷ 1.07³ = 1.225 | $857.96 |

$$\text{Bond Price} = \$46.73 + \$43.67 + \$857.96 = \$948.36$$
The bond trades **below par** ($1,000) because its coupon rate (5%) < market yield (7%).

---

### Dividend Discount Model — Gordon Growth Model
$$P_0 = \frac{D_1}{r - g}$$

| Component | Definition |
|---|---|
| **Numerator $D_1$** | Next year's expected dividend per share = $D_0 \times (1 + g)$ |
| **Denominator $(r - g)$** | Required return minus the perpetual dividend growth rate |
| **$r$** | Investor's required rate of return (cost of equity) |
| **$g$** | Constant annual growth rate of dividends (must be $< r$) |

**Interpretation:** The fair value of a stock equals the present value of its dividends growing at a constant rate forever.  
**Use case:** Valuing mature, dividend-paying companies with stable growth (utilities, blue-chip stocks).  
**Example:**  
Last dividend paid $D_0 = \$2.00$; dividends grow at 4%/year; required return = 9%.  
$$D_1 = \$2.00 \times 1.04 = \$2.08$$
$$P_0 = \frac{\$2.08}{9\% - 4\%} = \frac{\$2.08}{0.05} = \$41.60$$

---

## 15. Variance and Sensitivity Analysis

### Absolute Variance
$$\text{Variance} = \text{Actual} - \text{Budget}$$

| Sign | Revenue line | Cost line |
|---|---|---|
| **Positive** | Favorable — actual > budget | Unfavorable — actual > budget |
| **Negative** | Unfavorable — actual < budget | Favorable — actual < budget |

**Use case:** Monthly management reporting; identifying over- and under-performing areas.  
**Example:**  
Budgeted revenue: $500,000; Actual revenue: $470,000  
$$\text{Revenue Variance} = \$470,000 - \$500,000 = -\$30,000 \quad \text{(Unfavorable)}$$

---

### Variance %
$$\text{Variance \%} = \frac{\text{Actual} - \text{Budget}}{\text{Budget}} \times 100$$

| Component | Definition |
|---|---|
| **Numerator** | Absolute Variance = Actual minus Budget |
| **Denominator** | Budget = the planned or reference amount |

**Interpretation:** Expresses the variance as a percentage of the plan — useful for scaling comparisons across line items of very different sizes.  
**Example:**  
$$\text{Variance \%} = \frac{\$470,000 - \$500,000}{\$500,000} = \frac{-\$30,000}{\$500,000} = -6.0\%$$

---

### Profit Sensitivity to Volume
$$\Delta\text{Profit} = \text{Contribution Margin per Unit} \times \Delta\text{Volume}$$

| Component | Definition |
|---|---|
| **CM per Unit** | Profit added (or lost) for each additional (or fewer) unit sold |
| **ΔVolume** | Increase or decrease in units sold |

**Interpretation:** Fixed costs do not change with volume, so every unit above break-even adds exactly CM per unit to profit — and every unit below subtracts it.  
**Use case:** Scenario analysis ("what if sales drop 10%?"); quantifying downside risk quickly.  
**Example:**  
CM per Unit = $16; A supply disruption cuts volume by 800 units.  
$$\Delta\text{Profit} = \$16 \times (-800) = -\$12,800$$
The profit impact is an immediate $12,800 decline with no offset from fixed cost savings.

---

*All examples within each section use consistent numbers so the formulas can be traced and cross-referenced easily.*

---

## 16. Capacity and Operations

### Capacity Utilization Rate
$$\text{Capacity Utilization} = \frac{\text{Actual Output}}{\text{Maximum Possible Output}} \times 100$$

| Component | Definition |
|---|---|
| **Numerator** | Actual Output = units (or hours) actually produced in the period |
| **Denominator** | Maximum Possible Output = theoretical maximum at full capacity |

**Interpretation:** What percentage of total available capacity is being used.
- **< 70%** → Significant idle capacity; fixed costs are spread over fewer units, raising unit cost
- **70–85%** → Typical efficient operating range
- **> 90%** → Risk of bottlenecks, quality issues, and inability to handle demand spikes

**Use case:** Identifying whether a capacity investment is needed; diagnosing high unit costs in a manufacturing case.  
**Example:**  
A factory can produce 20,000 units/month at full capacity. It currently produces 14,000.  
$$\text{Capacity Utilization} = \frac{14,000}{20,000} = 70\%$$
The plant has 6,000 units/month of idle capacity — before building a new facility, management should ask why utilization is low (demand shortfall? supply constraint? scheduling?).

---

### Cost per Unit at Different Utilization Levels
$$\text{Unit Cost} = \frac{\text{Fixed Costs}}{\text{Actual Output}} + \text{Variable Cost per Unit}$$

| Component | Definition |
|---|---|
| **Numerator** | Fixed Costs = costs unchanged regardless of output (rent, depreciation, salaried staff) |
| **Denominator** | Actual Output = units actually produced |
| **Variable Cost per Unit** | Costs that scale directly with output (materials, direct labor) |

**Interpretation:** As output rises, fixed costs are spread over more units, so unit cost falls — this is **operating leverage**. Conversely, underutilization inflates unit cost.  
**Use case:** Explaining why a plant running at 50% utilization has uncompetitively high unit costs; pricing decisions.  
**Example:**  
Fixed Costs = $200,000/month; Variable Cost = $8/unit.

| Utilization | Units Produced | Fixed Cost per Unit | Variable Cost | **Unit Cost** |
|---|---|---|---|---|
| 50% | 10,000 | $20.00 | $8.00 | **$28.00** |
| 70% | 14,000 | $14.29 | $8.00 | **$22.29** |
| 100% | 20,000 | $10.00 | $8.00 | **$18.00** |

Running at 70% vs 100% costs an extra **$4.29 per unit** — purely due to underutilization.

---

### Bottleneck Throughput
$$\text{System Throughput} = \text{Bottleneck Capacity (units per period)}$$

$$\text{Bottleneck Utilization} = \frac{\text{Demand Rate}}{\text{Bottleneck Capacity}} \times 100$$

| Component | Definition |
|---|---|
| **Bottleneck** | The single process step with the lowest capacity — it limits the entire system |
| **Demand Rate** | Volume of orders or jobs arriving per period |

**Interpretation:** The output of an entire operation is capped by its slowest step. No amount of improvement elsewhere increases total throughput unless the bottleneck is addressed.  
**Use case:** Operations cases involving queues, factory floor redesign, or service capacity.  
**Example:**  
A 3-step assembly line: Step A = 500 units/hr; Step B = 320 units/hr; Step C = 450 units/hr.  
Bottleneck = Step B (320 units/hr) → System output is capped at **320 units/hr** regardless of Steps A and C.  
If demand = 400 units/hr:  
$$\text{Bottleneck Utilization} = \frac{400}{320} = 125\% \quad \Rightarrow \text{Backlog builds — Step B must be expanded}$$

---

## 17. Market Analysis

### Market Share (Value)
$$\text{Market Share \%} = \frac{\text{Company Revenue}}{\text{Total Market Revenue}} \times 100$$

| Component | Definition |
|---|---|
| **Numerator** | Company Revenue = the firm's sales in a defined market and period |
| **Denominator** | Total Market Revenue = all sales by all competitors in that same market |

**Interpretation:** The fraction of total market spending captured by the company.  
**Use case:** Competitive benchmarking; tracking whether growth is coming from market expansion or share gains.  
**Example:**  
The company earns $48M; total market = $320M.  
$$\text{Market Share} = \frac{\$48M}{\$320M} = 15\%$$

---

### Market Share (Volume)
$$\text{Market Share \% (volume)} = \frac{\text{Company Units Sold}}{\text{Total Market Units Sold}} \times 100$$

**Interpretation:** Share based on units rather than dollars. Comparing value share vs volume share reveals whether the company sells at a **premium** (value share > volume share) or a **discount** (volume share > value share).  
**Example:**  
Company sells 90,000 units; total market = 750,000 units.  
$$\text{Volume Share} = \frac{90,000}{750,000} = 12\%$$
Value share = 15%; Volume share = 12% → The company commands a price premium (it captures more revenue per unit than the average competitor).

---

### Relative Market Share
$$\text{Relative Market Share} = \frac{\text{Company Market Share}}{\text{Largest Competitor's Market Share}}$$

| Component | Definition |
|---|---|
| **Numerator** | The company's own market share |
| **Denominator** | The market share of the single largest competitor |

**Interpretation:** A ratio > 1.0 means the company is the market leader. Used in BCG matrix analysis: a relative share > 1× confers scale advantages in cost and brand.  
**Use case:** Competitive position assessment; portfolio strategy (Stars, Cash Cows, etc.).  
**Example:**  
Company share = 15%; Largest competitor = 25%.  
$$\text{Relative Market Share} = \frac{15\%}{25\%} = 0.6\times \quad \Rightarrow \text{The company is not the market leader}$$

---

### Market Growth Rate
$$\text{Market Growth Rate} = \frac{\text{Current Year Market Size} - \text{Prior Year Market Size}}{\text{Prior Year Market Size}} \times 100$$

| Component | Definition |
|---|---|
| **Numerator** | Absolute growth in total market size (revenue or units) year-over-year |
| **Denominator** | Prior year market size = the baseline |

**Interpretation:** How fast the overall market is expanding or contracting — distinct from the company's own revenue growth.  
**Use case:** Distinguishing organic growth from share gains; market attractiveness screening.  
**Example:**  
Market was $300M last year; it is $324M this year.  
$$\text{Market Growth} = \frac{\$324M - \$300M}{\$300M} = 8\%$$
If the company's revenue grew 15%, it outpaced the market by 7pp → it gained share.

---

### Total Addressable Market (TAM) — Bottom-Up Sizing
$$\text{TAM} = \text{Number of Potential Customers} \times \text{Average Annual Spend per Customer}$$

| Component | Definition |
|---|---|
| **Number of Potential Customers** | Everyone who could plausibly buy the product (segment the population if needed) |
| **Avg. Annual Spend per Customer** | Average dollars spent on this category per year |

**Interpretation:** The maximum revenue opportunity if the company captured 100% of the market.  
**Use case:** Market entry decisions; investor pitch sizing; setting growth ambition.  
**Example:**  
Target segment: 4 million small businesses in the country. Each spends ~$600/year on the software category.  
$$\text{TAM} = 4{,}000{,}000 \times \$600 = \$2.4\text{ billion}$$

---

## 18. Pricing and Revenue Decomposition

### Revenue Decomposition
$$\text{Revenue} = \underbrace{\text{Price}}_{\text{rate}} \times \underbrace{\text{Volume}}_{\text{quantity}}$$

$$\Delta\text{Revenue} = \underbrace{(\Delta\text{Price} \times Q_{\text{old}})}_{\text{Price effect}} + \underbrace{(\Delta Q \times P_{\text{new}})}_{\text{Volume effect}}$$

| Component | Definition |
|---|---|
| **Price effect** | Revenue change caused solely by the price change, holding volume constant |
| **Volume effect** | Revenue change caused by the volume change at the new price |

**Interpretation:** Any revenue movement can be split into what was driven by pricing versus what was driven by volume. This is the first diagnostic in any profitability case.  
**Use case:** Diagnosing a revenue decline — is it a pricing problem, a volume problem, or both?  
**Example:**  
Last year: 10,000 units at $30 = $300,000. This year: 8,500 units at $32 = $272,000 (−$28,000).

| Effect | Calculation | Amount |
|---|---|---|
| Price effect | +$2 × 10,000 units | +$20,000 |
| Volume effect | −1,500 units × $32 | −$48,000 |
| **Net change** | | **−$28,000** |

The price increase added $20K but volume loss cost $48K — the net effect is negative, so the price increase was not worth it.

---

### Revenue Growth Decomposition (3 drivers)
$$\text{Revenue Growth} = \underbrace{\text{Price Growth}}_{\%} + \underbrace{\text{Volume Growth}}_{\%} + \underbrace{\text{Mix Shift}}_{\%}$$

| Driver | Definition |
|---|---|
| **Price Growth** | Change in average selling price, holding mix and volume constant |
| **Volume Growth** | Change in total units sold, holding price and mix constant |
| **Mix Shift** | Revenue change from selling proportionally more high-price vs low-price products |

**Interpretation:** Revenue growth comes from three levers simultaneously; isolating each reveals which lever is driving (or dragging) performance.  
**Use case:** Explaining to an interviewer why revenue grew despite a price cut, or why it fell despite volume gains.  
**Example:**  
Revenue grew 6%. Breakdown: Average price −2% (competitive pressure); Volume +5%; Mix +3% (shift toward premium SKUs).  
The company is growing despite price erosion — it compensates through volume and premiumization.

---

### Price-Volume Tradeoff: Break-Even Volume Change
$$\Delta Q_{\text{break-even}} = \frac{-\Delta P}{\text{CM per Unit} + \Delta P}$$

| Component | Definition |
|---|---|
| **Numerator** | $-\Delta P$ = the revenue lost per existing unit due to the price reduction |
| **Denominator** | CM per Unit + ΔP = the new contribution per unit after the price change |

**Interpretation:** If you cut the price by $\Delta P$, how many *additional* units must you sell to keep total profit unchanged?  
**Use case:** Deciding whether a price cut or promotional discount is financially justified.  
**Example:**  
Current price = $25; Variable cost = $9; CM = $16. Considering a $3 price cut → new price $22, new CM = $13.  
$$\Delta Q_{\text{break-even}} = \frac{-(-\$3)}{\$16 + (-\$3)} = \frac{\$3}{\$13} = 23.1\%$$
You must sell at least **23.1% more units** just to break even on profit. If PED = −1.5 and the price cut is −12%, expected volume gain ≈ +18% — which falls short of 23.1%, so the price cut destroys profit.

---

### Optimal Price (Maximizing Revenue)
$$\text{Revenue-Maximizing Price} \Rightarrow \text{achieved when } |\text{PED}| = 1$$

For a linear demand curve $Q = a - bP$:
$$P^* = \frac{a}{2b}$$

**Interpretation:** Revenue is maximized at the price point where elasticity = −1 (unit elastic). Above this price, the % volume loss exceeds the % price gain; below it, the opposite is true.  
**Use case:** Setting an initial price for a new product; quick-check in pricing strategy cases.

---

## 19. Marketing and Promotions

### Marketing ROI (MROI)
$$\text{MROI} = \frac{\text{Incremental Gross Profit from Campaign} - \text{Marketing Spend}}{\text{Marketing Spend}} \times 100$$

| Component | Definition |
|---|---|
| **Numerator** | Net incremental profit = gross profit attributable to the campaign minus what was spent |
| **Denominator** | Marketing Spend = total campaign cost |

**Interpretation:** The profit return generated for every dollar spent on marketing. Unlike simple revenue ROI, this uses **gross profit** because the cost of goods must be subtracted first.  
**Use case:** Evaluating whether a campaign, channel, or promotion should be continued or scaled.  
**Example:**  
A digital campaign costs $50,000 and drives 2,000 incremental units sold. Price = $25; Variable cost = $9 → Gross profit/unit = $16.  
$$\text{Incremental Gross Profit} = 2,000 \times \$16 = \$32,000$$
$$\text{MROI} = \frac{\$32,000 - \$50,000}{\$50,000} = -36\% \quad \Rightarrow \text{Campaign loses money — redesign or cut}$$

---

### Return on Ad Spend (ROAS)
$$\text{ROAS} = \frac{\text{Revenue Attributable to Ad Spend}}{\text{Ad Spend}}$$

| Component | Definition |
|---|---|
| **Numerator** | Revenue (not profit) directly driven by the advertising |
| **Denominator** | Total advertising spend in the same period |

**Interpretation:** How many dollars of revenue are generated per dollar of advertising. Note: ROAS uses *revenue*, not profit — a high ROAS can still be unprofitable if margins are thin.  
**Use case:** Comparing efficiency across ad channels (search, social, display).  
**Example:**  
Ad spend = $50,000; Attributed revenue = $200,000.  
$$\text{ROAS} = \frac{\$200,000}{\$50,000} = 4.0\times \quad \Rightarrow \text{Every \$1 of ad spend returns \$4 in revenue}$$
But if gross margin is only 20%, gross profit = $40,000 < ad spend ($50,000) → still unprofitable.

---

### Promotional Lift
$$\text{Promotional Lift \%} = \frac{\text{Sales during Promotion} - \text{Baseline Sales}}{\text{Baseline Sales}} \times 100$$

| Component | Definition |
|---|---|
| **Numerator** | Incremental sales = actual sales minus what would have been sold without the promotion |
| **Denominator** | Baseline Sales = expected sales in the same period absent any promotion |

**Interpretation:** How much extra volume (%) the promotion generated above the normal run-rate.  
**Use case:** Measuring whether a promotion actually drove incremental demand or simply pulled forward future purchases.  
**Example:**  
Baseline weekly sales = 5,000 units. During the promotion = 6,800 units.  
$$\text{Lift} = \frac{6,800 - 5,000}{5,000} = 36\%$$

---

### Break-Even Sales Lift for a Promotion
$$\text{Required Lift \%} = \frac{-\Delta\text{CM per Unit}}{\text{New CM per Unit}} \times 100$$

| Component | Definition |
|---|---|
| **Numerator** | $-\Delta\text{CM}$ = reduction in contribution margin per unit caused by the discount |
| **Denominator** | New CM per Unit = contribution margin after the discount is applied |

**Interpretation:** The minimum percentage volume increase the promotion must generate for total profit to remain unchanged.  
**Use case:** Deciding whether to run a price promotion; evaluating trade deal terms from a retailer.  
**Example:**  
Normal price $25; Variable cost $9; CM = $16. Promotion offers $4 off → new price $21; new CM = $12.  
$$\text{Required Lift} = \frac{\$4}{\$12} = 33.3\%$$
The promotion must drive at least **33.3% more volume** to break even on profit. Pair this with your PED estimate to judge feasibility.

---

## 20. Competitive Analysis

### Herfindahl-Hirschman Index (HHI) — Market Concentration
$$\text{HHI} = \sum_{i=1}^{n} s_i^2$$

| Component | Definition |
|---|---|
| **$s_i$** | Market share of firm $i$ expressed as a whole number (e.g., 30 for 30%) |
| **$n$** | Number of firms in the market |

**Interpretation:**
- **HHI < 1,500** → Competitive (unconcentrated) market
- **1,500–2,500** → Moderately concentrated
- **> 2,500** → Highly concentrated / near-monopoly

**Use case:** Assessing competitive intensity in an industry case; understanding M&A regulatory risk.  
**Example:**  
Four firms with shares of 40%, 30%, 20%, 10%:  
$$\text{HHI} = 40^2 + 30^2 + 20^2 + 10^2 = 1,600 + 900 + 400 + 100 = 3,000$$
HHI = 3,000 → Highly concentrated market. A merger between the top two firms would face significant antitrust scrutiny.

---

### Price Premium vs. Competitor
$$\text{Price Premium \%} = \frac{\text{Company Price} - \text{Competitor Price}}{\text{Competitor Price}} \times 100$$

| Component | Definition |
|---|---|
| **Numerator** | The absolute price difference between the company and the reference competitor |
| **Denominator** | Competitor Price = the benchmark (usually the market average or the largest rival) |

**Interpretation:** How much more (or less) the company charges relative to the competition. A positive premium is only sustainable if backed by differentiation customers value.  
**Use case:** Pricing strategy; diagnosing volume share loss; brand positioning analysis.  
**Example:**  
Company price = $32; main competitor = $27.  
$$\text{Price Premium} = \frac{\$32 - \$27}{\$27} = 18.5\%$$
If volume share is declining, ask: has the premium grown (price-driven loss) or has perceived differentiation eroded (brand-driven loss)?

---

### Competitive Response: Profit Impact of a Competitor Price Cut
$$\Delta\text{Profit (if we do not respond)} = -\Delta Q_{\text{lost}} \times \text{CM per Unit}$$

$$\Delta\text{Profit (if we match the cut)} = (\text{Q}_{\text{retained}} \times \Delta\text{CM}) + (\text{incremental Q won back} \times \text{new CM})$$

**Interpretation:** When a competitor cuts price, you face two options — do nothing (lose volume) or match (keep volume but at lower margin). Quantifying both is the first step in a competitive response analysis.  
**Use case:** Competitive dynamics cases; deciding whether to start or join a price war.  
**Example:**  
A competitor cuts price by $3. You estimate you'll lose 1,200 units/month if you don't respond.  
Current CM = $16/unit.  
$$\text{Profit impact of doing nothing} = -1,200 \times \$16 = -\$19,200/\text{month}$$
If matching the cut reduces CM from $16 to $13 but retains all 8,000 units:  
$$\text{Profit impact of matching} = 8,000 \times (\$13 - \$16) = -\$24,000/\text{month}$$
In this case, **not responding** is less costly — unless the volume loss compounds over time.

---

## 21. Operating Leverage and Cost Structure

### Operating Leverage
$$\text{Operating Leverage} = \frac{\text{Contribution Margin}}{\text{Operating Profit (EBIT)}}$$

| Component | Definition |
|---|---|
| **Numerator** | Contribution Margin = Revenue − Total Variable Costs |
| **Denominator** | Operating Profit (EBIT) = Contribution Margin − Fixed Costs |

**Interpretation:** How many times larger the contribution margin is relative to operating profit — tells you how sensitive profit is to a change in revenue.
$$\% \Delta\text{Operating Profit} \approx \text{Operating Leverage} \times \% \Delta\text{Revenue}$$
A high fixed-cost business (e.g., airlines, software) has high operating leverage: small revenue swings cause large profit swings.  
**Use case:** Assessing profit sensitivity in scenario analysis; explaining why a business is risky in a downturn.  
**Example:**  
Revenue = $96,000; Variable costs = $32,000; Fixed costs = $52,000.  
CM = $64,000; EBIT = $12,000.  
$$\text{Operating Leverage} = \frac{\$64,000}{\$12,000} = 5.3\times$$
If revenue falls 10%:  
$$\% \Delta\text{EBIT} \approx 5.3 \times (-10\%) = -53\%$$
A 10% revenue drop wipes out more than half of operating profit.

---

### Fixed vs. Variable Cost Ratio
$$\text{Fixed Cost Ratio} = \frac{\text{Total Fixed Costs}}{\text{Total Costs}} \times 100$$

| Component | Definition |
|---|---|
| **Numerator** | Fixed Costs = costs that do not change with output level |
| **Denominator** | Total Costs = Fixed Costs + Total Variable Costs |

**Interpretation:** Businesses with a high fixed cost ratio have high operating leverage — profitable when running near capacity, but vulnerable in downturns. Businesses with a high variable cost ratio are more resilient but have lower upside.  
**Use case:** Quickly characterizing a business model's risk profile in an industry case.  
**Example:**  
Fixed costs = $200,000; Variable costs at current volume = $80,000; Total costs = $280,000.  
$$\text{Fixed Cost Ratio} = \frac{\$200,000}{\$280,000} = 71.4\%$$
This is a high fixed-cost business (e.g., manufacturing, hospitality) — profits are highly sensitive to volume changes.

---

### Profit Impact of a Cost Change
$$\Delta\text{Profit} = -\Delta\text{Cost per Unit} \times \text{Volume}$$

| Component | Definition |
|---|---|
| **$\Delta$Cost per Unit** | Change in variable cost per unit (positive = cost increase, negative = saving) |
| **Volume** | Current units sold |

**Interpretation:** A variable cost saving flows directly to profit (dollar for dollar) across all units sold. Fixed cost changes flow to profit in full regardless of volume.  
**Use case:** Quantifying the profit impact of a supplier price increase, wage change, or efficiency improvement.  
**Example:**  
A $1.50/unit increase in raw material costs; current volume = 80,000 units/year.  
$$\Delta\text{Profit} = -\$1.50 \times 80,000 = -\$120,000/\text{year}$$
To offset this, the company must either raise prices, cut other costs, or grow volume.

---

*Sections 16–21 cover the quantitative tools most commonly tested in case interviews beyond standard financial statements.*
