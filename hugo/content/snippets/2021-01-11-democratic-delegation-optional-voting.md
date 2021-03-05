+++
title = "Democratic Delegation-optional Voting"
date = 2021-01-11T00:00:00
uid = "k6m4tVFrq"
tags = ["taking-silly-ideas-seriously"]
keywords = ["delegation", "voting"]
+++

In this snippet I propose a novel voting system, which I call "Democratic Delegation-optional Voting". The core idea of the voting system is that anyone can choose to delegate their vote to a group or individual that they trust. They may change their delegate selection at any time and for any reason (including for a brief period after votes are cast, as we will see), or they may choose to cast a vote themselves rather than delegating their vote.

## What problem does this voting system solve?

Individual voters don't have enough time or energy to research every issue up for vote. So, delegation is crucial. At the same time, voters shouldn't yield their power to delegates entirely. If a voter feels passionately about an issue, they should not have to hope their representative's views align with theirs.

## How does the system work?

Ahead of a Vote, an individual or organization can register themselves as a Delegate. They need only do this once even if there will be many Votes. 

On its own, a Delegate has no voting power. Each voter gets one ballot. Each voter may choose to cast that ballot themselves, or they may delegate their ballot to a Delegate.

Similarly, a Delegate may choose to cast its ballots itself, or it may choose to delegate them to another Delegate. If ten people have delegated their ballots to a Delegate, then it has ten times the voting power of an individual. A Delegate's votes or delegation selections are public, whereas an individual's votes or delegation selections are private.

Votes may be cast or a Delegate selected at any time leading up to a Vote deadline. Votes may be modified and Delegate selections may be changed up until this deadline.

Once the Vote deadline arrives, votes and delegation-selections made by Delegates are made public. Delegates can no longer change their selections at this point. Individual voters then have an additional 48 hours following the Vote deadline during which they may choose to modify their ballot.

The system is flexible, in that it is compatible with winner-take-all voting, ranked choice voting, approval voting, proportional representation, etc.

## Toy Example: Playground Election

We now demonstrate the voting system in a playground setting.

Aaron, Brianna, Chloe, Daniel, and Emily are playing on the playground. Aaron and Brianna both want to use the swing. There's only one swing. "Let's vote!" suggests Emily. "Whoever gets more votes gets to swing." Aaron and Brianna agree: whoever gets three or more votes wins. Daniel shrugs. "Chloe can have my vote!" he shouts, and he runs off to play alone on the seesaw.

So Aaron, Brianna, Chloe and Emily each vote: Aaron and Brianna each for themselves, Chloe for Aaron and Emily for Brianna.

"So Aaron wins, 3-2, since Chloe's vote also counts for Daniel!" Emily shouts. She's really getting into this election thing.

Just then Daniel comes tearing around the corner. "Wait! I thought you were going to vote for Brianna", he tells Chloe. "Can I change my vote?"

Emily, having studied _Democratic Delegation-optional Voting_ says "Sure, no trouble. Anyone else?" Hearing no other vote-changes, she proclaims Brianna the winner, and Aaron spends the rest of recess helping push Brianna higher on the swing.

## Another Example: Local and State Legislation

For this example, consider a hypothetical local government and state government both using _Democratic Delegation-optional Voting_. Over the next two weeks, the local government will be voting on two issues (the school budget and a commercial cannabis restriction ordinance), and the state government will also be voting on two issues (an unpopular jaywalking penalty and an obscure contract law thingy that affects very few people and is hard to understand).

Many of the residents have set up simple _rules_ for choosing default Delegates. Several republican residents, they have selected their local republican Delegate as their default Delegate, and similarly several democratic residents have selected the local democratic Delegate as their default Delegate. Some residents have a rule-based system, where e.g. education-related issues are delegated to one Delegate while penal code issues are delegated to another.

The Vote deadlines are set as follows, and the text of each issue is made available to the public two weeks prior to its Vote deadline:

Local school budget: January 21, 2021

State unpopular jaywalking penalty: January 22, 2021

Local commercial cannabis restriction ordinance: January 28, 2021

State obscure contract law thingy that affects very few people and is hard to understand: January 29, 2021

Many of the residents hear about the unpopular jaywalking penalty, and they see how awful an idea it is, and so they directly submit a Nay vote on that issue. The penalty is overwhelmingly voted down.

The school budget is a popular but particularly nuanced issue. While many residents chose to vote on it directly, we also see many residents choose a Delegate that they trust with school board issues, since they know this vote is important but complicated.

For many people, the commercial cannabis restriction ordinance is an important issue too, but they trust their default Delegate will vote appropriately. The day after the election they're surprised to read on their social media newsfeed of choice that one of the common default Delegates didn't vote as expected, so they double check their vote. The vote looks fine. Clickbait post, I guess.

Many of the residents don't care about the obscure contract law thingy that affects very few people and is hard to understand, and so they leave their default Delegate selected. Some of the common default Delegates also don't have time for obscure contract law, and so they choose to delegate their votes to still further, more specialized Delegates that they trust. (This is good because not only do most voters not have time to look into contract law, they also don't have time to look into people who do have time to look into contract law, so they trust their Delegate to do _that_.) Most of the voters are fine with how their vote ends up being cast, though a few don't like the sub-Delegate their default-Delegate chose, and so those few can change their vote if they like.

In all cases, the final votes are in and the election is tallied 48 hours after the election deadline. The school budget passes. The jaywalking penalty is voted down. The commercial cannabis restriction ordinance will go into effect immediately. And the obscure contract law thingy that affects very few people and is hard to understand... well, to be honest I didn't really follow that one too closely.

## Some observations

You've seen the _Democratic Delegation-optional Voting_ in action now. It's "democratic", because it gives everyone an equal voice in every election. Everyone gets precisely one vote. It's "delegation-optional" because voters and Delegates alike have the choice of whether to vote directly, delegate their vote, or even skip voting altogether.

You'll notice that there are no explicit elected representatives in this system. There are merely different degrees of being an elected representative (the number of ballots you are responsible for as a Delegate). Anyone can register as a Delegate, and whether you make this a full-time job, investigating every single issue on the table, or whether you often delegate your votes further is up to you as a Delegate. Under this system, some common Delegates will be responsible for casting huge numbers of votes, while other Delegates will be responsible for casting just a handful.

I mentioned that either an individual or an organization can register as a Delegate. If an organization registers as a Delegate they can select their votes through whatever process they choose (e.g. an internal election is fair game), and they are held to the same deadlines as every other Delegate.

## Some edge-cases and minor details

As mentioned in the Local and State Legislation example, a voter can set up simple rules for selecting their default Delegate. The voting system can also be extended to allow a voter to additionally specify "fall-through" backup Delegates. A ballot is given to a fall-through Delegate in the case that a voter's higher-priority Delegate does not take an action on a particular piece of legislation.

What happens if a major Delegate delegates their ballots to a trusted specialized delegate, but isn't happy with how that trusted specialized delegate votes? They can contact their constituents and let them know. The constituents will have 48 hours during which they can change their vote.

What happens if a Delegate A delegates their ballots to Delegate B, and Delegate B delegates their ballots to Delegate A? This should be easy to avoid in practice, because I expect Delegates will naturally have clear roles / specializations. Should it occur, however, no vote will be cast for voters delegating their ballot to those Delegates (unless a voter listed a backup Delegate), and the voters will have the usual 48 hours during which to place their vote.

## Conclusion

_Democratic Delegation-optional Voting_ truly puts governance in the hands of the people, without needing everyone to be an expert on everything. It makes Delegates accountable to their constituents, because a constituent can change their Delegates at any time. It allows people to perform their civic duty to precisely the extent that is appropriate for them. On the issues that matter most to them, they can cast an explicit vote. For the majority of issues, though, individuals don't need to learn the details of every piece of legislation. They have the option to trust those to their Delegates.
