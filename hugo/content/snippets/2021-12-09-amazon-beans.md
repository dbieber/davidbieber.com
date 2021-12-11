+++
title = "Amazon Beans: Only Pay for What You Eat"
date = 2021-12-09T00:00:00
tags = ["taking-silly-ideas-seriously"]
+++

The idea is simple, it's silly, but I think it has surprising depth.
It's Amazon Beans: "only pay for what you eat".

Basically, I envision a new product from Amazon
(or any other retailer, but it feels like a very Amazon idea, as you'll soon see):
a special case of cans of beans.
What makes it special?
You don't have to pay anything to receive the case.
You only pay for the cans of beans that you remove from the case.

So, the actual tagline would be "only pay for what you open",
but I thought "only pay for what you _eat_" had a better ring to it,
and still describes the situation fairly accurately.


#### Straw man implementation of Amazon Beans

The implementation details are left to the retailer to determine, but I'll put out a straw man just to provide evidence that the Amazon Beans idea is possible to put into practice.
Here's the straw man:
The buyer must provide payment details to get the case of Amazon Beans, but they are not charged anything up front.
The case of Amazon Beans is internet connected, with little sensors that indicate
when cans of beans are removed.
The purchaser of the case agrees to pay for any beans that are removed from the case. And if for some reason the case cannot phone home for a while, e.g. because it's thrown in a Faraday cage for a week or something like that, the purchaser will pay for the full case of beans.
If the beans are never eaten, they are never paid for[^1].
Once they are eaten, they are considered purchased, but even then they don't need to be paid for immediately; further deferred payment services are available as well.

[^1]: The shelf-life of beans tends to be 2-5 years, so the policy can be something like: "If the beans remain uneaten for 5 years, you get to keep the beans for free. Dispose of them responsibly."


#### Why Amazon Beans?

Possible consequences of an Amazon Beans program include:

- Ending world hunger
- Increasing global resilience to supply chain shocks
- Further cementing Amazon's market dominance
- Giving increased flexibility to people living paycheck to paycheck

In one sense, Amazon Beans turns ordinary homes into an extended Amazon warehouse.
Since the beans can be delivered and consumed at vastly different points in time,
this adds flexibility to delivery logistics, acting as a shock-absorber of sorts for changes in supply chain and shipping.

A family that lives paycheck to paycheck might not have sufficient funds to keep a reserve of extra food in their home if they have to pay for that food up front, but if the food is only paid for once it is eaten, this program might allow that family to maintain such a food reserve.
If they are temporarily between jobs, the food is still available without the hassle of having to take out a loan and go into debt to acquire it (kind of... eating food you cannot afford is still like going into debt, but it ought to be a smoother experience and importantly it doesn't leave the family _without food_ at any point).


#### More implementation thoughts

**Internet connectivity**
When you get your first case of Amazon Beans (or when you order it),
you need to tell it how to connect to the internet.
You don't need to do this for subsequent cases of beans though.
The internet connectivity information can be stored by Amazon and come
preconfigured on all future Amazon Beans cases that you order.
This way, when they arrive, you can just toss them on your shelf.

**Stockpiling**
Customers are by default only allowed to order a single case of Amazon Beans at a time, and only when they've consumed a certain fraction of that case can they order their next case.
(And if they opt in, that next case can be ordered automatically, at no cost to the consumer, when the first case is running low.)
This eliminates any worry Amazon might have about a single adversarial customer
ordering a large quantity of beans and letting them all go unused and unpaid for.
After a customer earns trust (e.g. by demonstrating they are a restaurant or that they consume beans in higher quantities), they can order a larger shipment of Amazon Beans cases.


#### What products make sense?

Beans are a good candidate for the Amazon Beans model because they are inexpensive, ship well in bulk, have a long shelf life,
and have a predictable repeating consumption pattern.
Other products might make sense too.
Other foods like pastas, rice, canned foods, tea, powdered milk, jerky, etc have similarly long shelf-lives and could make sense.
Repeatedly consumed products like toothpaste, batteries, and toilet paper likely make sense too. These are the types of products that Amazon already encourages subscriptions for.


#### Tangent: Dorm Supply

Related to Amazon Beans, but extended to a wider variety of products, we end up at the idea of a low-cost / no-money-down reseller. Instead of considering this in the context of a single household, let's consider the lobby of an 80-person dormitory. The dorm manager orders (at no cost to the dorm) products that the students living there are likely to use. The students are only charged if they take the product. When summer comes, unused product is returned or saved for the following year. If the product has a limited shelf-life, unconsumed product is disposable at no cost at the end of the shelf-life.


#### Risks and Risk Mitigation

The primary risk to Amazon is that product is ordered but goes unconsumed, and therefore is never paid for.
The anti-stockpiling measure described above takes one step to mitigate this risk.
I don't actually think the risk is that large, but of course it would be necessary to model and monitor this risk if putting the Amazon Beans program into production.
Another risk mitigation measure is that
Amazon could charge a small nominal fee for the first case of Amazon Beans. Adding this entry fee for the program will prevent people from ordering cases of beans that they have no intention of consuming.
This fee could even go toward the costs of the beans, so it doesn't even feel like a fee to the consumer.

Another risk of the program is
it comes with a feeling of spending associated with each can opened.
This is not good for the consumer's mental health,
and it discourages consumption. Feeling like you're spending money every time you go to eat in your own house is an uncomfortable situation.
Feeling like your eating habits are being monitored is similarly uncomfortable.
I don't have any mitigation strategies to offer for these issues at this time.

Another risk comes in scaling to many products. If ordering a case of a product is truly no cost to a consumer, they would order a case of every possible product.
That doesn't work as the product offerings soar to thousands of products.
Having the nominal up-front cost mentioned above, which goes toward the cost of the first units of the product consumed, mitigate this and allow for scaling.

Finally, a consumer's tastes may change. They may have a case of a product they don't want to consume ever again. Being able to return large quantities of a product is important for situations like this.


#### Directions for Future Snippets

In a future snippet it would be interesting to consider the costs and benefits to Amazon and to the consumer of an Amazon Beans program.
I expect we'll find that if the cost of internet connectivity is modest relative to the cost of a case of beans, this becomes a win-win for a large segment of consumers and for Amazon.
Some costs to consider include spoilage and other lost beans, customer service, cost of beans, shipping costs, software costs, and of course the cost of the special internet-connected case.

In a future snippet I'd also like to think through whether I'm a proponent of the idea. What are the longer term consequences? What ethical issues arise?

Brainstorming fun names comes later too. Jeffrey Beanzos? I'll keep thinking.
