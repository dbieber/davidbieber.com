+++
title = "Amazon Cloud Kitchen"
date = 2021-12-20T00:00:00
tags = ["taking-silly-ideas-seriously"]
+++

This snippet is about a fake future service that Amazon could offer one day called Amazon Cloud Kitchen. It's the food analog of Amazon's existing (real) Amazon Cloud Services offerings.

The core idea with Amazon Cloud Kitchen is that users can submit recipes programmatically to the Cloud Kitchen, where a nearby warehouse of robotic chefs will automatically prepare the recipe. Once prepared it will be delivered in less than two hours, still warm, to your residence or restaurant.

When you picture robotic chefs, you may be imagining a metallic biped with a chef's hat. That's not what's is happening behind the scenes in Amazon's Cloud Kitchen.
Instead, a series of highly modular rectangular units on rails
are performing a carefully orchestrated and optimized series of cooking tasks to prepare tens of thousands of recipes concurrently.

Each recipe declaratively defines what ingredients and instruments are needed, and how they are combined.
Interchangeable robotic ovens, whisks, blenders, food dispensers, and arms zoom around the warehouse on rails completing the recipes, packaging the results, and sending them to shipping.

As with Amazon's other "Elastic" Cloud products, Amazon Cloud Kitchen scales whether you're making a single cupcake or food to feed a football stadium. Of course, the per-unit costs decrease as the amount of food your submitting for preparation increases, same as it does when reserving compute units in AWS.

The true beauty of Amazon Cloud Kitchen is the versatility it offers. Any recipe can be submitted, no matter how complicated the steps, no matter what the ingredients; it doesn't matter if it's a recipe that's never been made before, that you couldn't possibly buy prepared from a store. Since Amazon Cloud Kitchen uses automation to follow your recipe step-by-step, you can make recipes that suit precisely your needs.

This means it can respect your dietary needs.
Let's say you find a cake recipe on GitHub, complete with the g-code for applying the frosting pattern at the end, but it uses regular flour, whereas you want gluten-free flour.
Simply change the recipe and submit; no trouble.

At a low level, recipes are expressed as source code.
The programming language allows mixing declarative constructs ("X is Y mixed with Z") and procedural ones ("do X, then do Y" / "when X occurs, do Y").
For inspiration for language design we can look at [Cook](https://github.com/MichaelBarney/cook), but I think we can do better (an idea for a future snippet).
At a higher level, I don't think it's too much to ask to automatically translate human-friendly recipes into computer friendly ones. This is a challenging task, but possible with today's technology.

One of the benefits Amazon Cloud Kitchen gets from
its scale is the ability to forecast resource requirements. By looking at usage patterns, Amazon can ensure that each warehouse is stocked with adequate ingredients to meet the demand of the incoming programmatic recipes.

Amazon can further provide accurate just-in-time price and timing estimates. If a warehouse is out of an ingredient and someone tries to submit a recipe that requires that ingredient,
the user can receive a confirmation notice indicating that the ingredient is on delay, and that the recipe would not be processed until some later period.

For some users this is not a problem; if you're catering a large event, you'll likely place your order well in advance anyway. Of course, you can specify the delivery time in the future; you're not limited to just-in-time orders.
Recurring and scheduled orders further allow Amazon to ensure the warehouses are stocked at the appropriate times to meet the demand.

One challenge is dealing with allergies and food restrictions, such as avoiding nuts and keeping kosher. In order to service users with such restrictions, Amazon needs to
ensure the modular cooking components are properly cleaned and separated as appropriate. This seems well within the scope of designing the Cloud Kitchen warehouse.

Let's consider some example modules that would exist in the Cloud Kitchen, starting with the oven.
Recipes require baking at temperatures ranging from at least as low as 350°F to at least as high as 450°F.
Throughout the day as different recipes come in, the number of units of food requiring each different temperature will vary.
So, a possible module design for a Cloud Kitchen oven would be a long oven, 350°F at one end, and 450°F at the other end.
In between would be regions at the intervening temperatures.
As more or less space at different temperatures is needed,
different regions in the oven can be set to different temperatures.
We can view this as shifting the temperature change points left and right along the oven.
The advantage of this design is we minimize the amount of temperature changes (pre-heating and cooling) needed, allowing for faster completion of the recipes without wasting energy leaving the oven unused for any length of time.

Note that this implementation of baking means that "preheat" instructions typically found in recipes do not literally translate to a "preheat" action taking place in the Cloud Kitchen. This doesn't mean the recipe needs to be modified though; existing recipes found around the internet should work with Cloud Kitchen just fine. The recipe compiler that translates the recipe into specific instructions for the Cloud Kitchen will simply have to realize that a preheat instruction for an oven indicates that a heated oven is needed in the next step, not that the recipe requires starting with a non-preheated oven.[^1]

[^1]: A related language feature for the recipe programming language:
implicit variables. In recipes, there is usually only ever a single object of a given type (e.g. recipes rarely use two ovens). Sometimes there are multiple objects of the same type (e.g. two bowls of ingredients). If a recipe refers to an object by its type, it doesn't need to have any additional identifying information about that object, unless there is ambiguity. So, when you make a statement about an oven in a recipe, it's implied that your recipe now requires an oven. Future references to an oven imply the same oven; if you want to talk about a distinct oven, you can name them or indicate which oven you're talking about by specifying additional detail ("the 400°F oven" and "the 350°F oven"). In a future snippet we can sketch out what the language would look like, including writing the programs for a handful of example recipes.

Let's consider next another critical component of the Cloud Kitchen: food storage. During the preparation of a recipe, the intermediate ingredients need to be kept in containers.
The containers of food will need to be combined, shaken, stirred, boiled, heated, cooled, chopped, smashed, strained, kneaded, folded, diced, blended, etc.
Importantly, the food storage units should be standardized and compatible with all of the food processing units they will be needed with.

When a recipe is compiled (when it is converted from source code to a series of precise steps to be executed by the Cloud Kitchen), all of the requirements for the containers will be computed ahead of time. A suitable container will then be selected. This container will be of the appropriate size to hold all the ingredients that will eventually be added, and it will be compatible with all the other implements it will be used with (e.g. blending-compatible, freezing compatible, etc).

The next step is to build the "Cloud Kitchen simulator" as an interesting environment in which to explore optimization techniques, and to design the Cloud Kitchen before actually getting funding and starting to build it.
When setting up the simulator, we can define the layout of the warehouse, define where ingredients will be housed, what kinds of modules are available, how reliable they are, what distribution of recipes will be coming in, etc.
We could even simulate fires and maintenance and other adverse events to ensure we've truly thought through everything and that the Kitchen is ready to scale.

As more data about Cloud Kitchen usage comes in, and as innovation in modular components progresses, Amazon can regularly improve the layout and management of the Cloud Kitchen, reducing prices over time.
Optimizing the arrangement of ingredient stores, immovable modules (e.g. fixed ovens, refrigeration, etc), and rails for movable modules seems like an exciting and interesting challenge for the next generation to tackle.

I would love to see Amazon introduce their first Cloud Kitchen in the middle of a city, an uncommon choice for a warehouse. By putting a Cloud Kitchen in a city center,
there could be a pickup option, not just delivery.
Residents could have their perfect customized lunch ready for them when they're ready for it.

Not into the Amazon Cloud Kitchen idea?
Consider instead a nice case of [Amazon Beans](/snippets/2021-12-09-amazon-beans/).
