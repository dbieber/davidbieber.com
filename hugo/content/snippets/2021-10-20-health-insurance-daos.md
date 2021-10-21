+++
title = "Health Insurance DAOs"
date = 2021-10-20T00:00:00
tags = ["blockchain", "healthcare", "taking-silly-ideas-seriously"]
keywords = ["governance"]
+++

I've recently been learning about blockchain tech including Ethereum, smart contracts, and DAOs (distributed autonomous organizations).
With this snippet I want to explore the idea of using a DAO as a substitute for traditional health insurance.
Brainstroming here, I'm also intrigued by the ideas of (1) bringing [democratic delegation-optional voting (DDoV)](/snippets/2021-01-11-democratic-delegation-optional-voting/) into a DAO, (2) implementing a union as a DAO for collective bargaining, and (3) using smart contracts for international agreements [to avoid climate problems like this](https://www.nytimes.com/2021/10/20/climate/fossil-fuel-drilling-pledges.html). These are ideas for future snippets.

Health insurance at its core is about pooling people's resources to collectively pay for their healthcare.
Typically pooling takes the form of paying premiums to an insurance company.
When healthcare is necessary, someone files a claim and -- subject to the claim's approval -- the insurance company pays for the customer's healthcare.
Most users of health insurance pay more in premiums than is paid out by the health insurance company, and so overall the health insurance company makes money.
But if a customer ever incurs high costs of healthcare, they don't have to bear those costs themself; the insurance company will pay the costs.

If we're to use a DAO in place of a traditional health insurance company, the overall structure remains the same.
Customers become members of the health insurance DAO (henceforth, "HIDAO") by regularly paying a premium to the HIDAO.
Every month in exchange for paying your premium to the HIDAO, you receive a token.
This token indicates your membership in the HIDAO, enabling you to file a claim to receive reimbursement for healthcare costs.
In the first version of the HIDAO, an existing claims adjudication company can be used to validate claims.
A smart contract would use [the oracle pattern](https://ethereum.org/en/developers/docs/oracles/) to interface with the adjudicators.
When the adjudicators approve a claim, the HIDAO's smart contract automatically processes it, thereby paying the customer for their healthcare.

This set up enables some interesting possibilities beyond what's possible with traditional health insurance.

First is lower costs. Since there is no centralized for-profit institution here, all excess premiums can be returned to shareholders (the customers themselves!) as dividends. The HIDAO needs to keep some reserves in order to be able to process any unexpected spike in claims or healthcare costs. Beyond this reserve level are funds that would traditionally be operating expenses or profit. Operating expenses are quite low in a DAO (the main ones for the HIDAO would be gas and adjudication costs). By returning the profits to the customers, and by keeping operating expenses low with smart contracts, the costs of health insurance can be kept low.

Second is collective negotiation of rates. Traditional insurance companies negotiate rates with providers. This process can be distributed, taking advantage of the distributed governance that DAOs enable to allow participants in the DAO to collectively negotiate rates. This idea requires elaboration in a future snippet. [DDoV](/snippets/2021-01-11-democratic-delegation-optional-voting/) may be essential to allowing governance to continue smoothly despite potential voter apathy. We can write the smart contract with a mechanism to incentivize participants to negotiate good rates for the HIDAO, e.g. by monetarily rewarding those who negotiate favorable rates.

Third is **Collective Adjudication Overriding**. Insurance companies notoriously get adjudication wrong some of the time. With a HIDAO, the risk of this could be greater if we're not careful about setting up an appeal process, because the logic of a smart contract by default cannot be overruled. However, we have the option of building into the HIDAO's smart contracts the ability to collectively override the normal adjudication process. We can writ the smart contract such that if members of the HIDAO collectively decide that a claim adjudication decision was invalid, they can collectively override that decision.

Fourth is supporting investing in the HIDAO. The HIDAO could issue tokens (e.g. the tokens given to customers each month) that indicate who is to receive the dividends mentioned in the first point above. Perhaps this could improve the robustness of the HIDAO. This is something to explore more later.

Fifth is **Distributed Adjudication**. This is a potential way to replace the traditional adjudication company described in the core idea above. The idea here is that we can incentivize people to submit only valid claims, and we can incentivize people to do proper claims adjudication. This idea deserves further elaboration in a future snippet.

Lastly I have an open question: How do you handle someone who has both traditional and HIDAO health insurance? How is double filing of claims prevented in traditional health insurance? Let's say someone expects high healthcare costs. What's stopping them from signing up with two health insurance companies and filing claims with both of them? Probably the terms and conditions and the law. This sounds difficult to account for in the HIDAO smart contract, which ideally need not know about people's other real world contracts with other health insurance companies.

I'm optimistic about this idea. I think that if done well, it could outcompete traditional health insurance. Obviously health insurance is a complicated industry and this is just a quick brainstorming, so the idea has many iterations to go. The ultimate goal is to ensure good health outcomes for everyone, and a part of the story necessarily is bringing down healthcare costs across the board. This is just one piece of that story, but I suspect it may be an importance piece.
