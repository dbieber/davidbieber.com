+++
title = "DDoV for DAOs"
date = 2021-11-02T00:00:00
tags = ["blockchain"]
keywords = ["governance"]
+++

I wrote up the idea for [Democratic Delegation-optional Voting (DDoV)](/snippets/2021-01-11-democratic-delegation-optional-voting/) back in January. This was before I learned about DAOs (decentralized autonomous organizations). I think the idea is even more relevant in the context of DAOs than it was originally, and I'm intrigued to revisit it now that I am learning about DAOs.

The core of the idea is a governance structure that supports ad hoc delegation of votes. Since there are potentially many things to vote on, but not everybody is invested enough or has enough time to learn about and vote on all of them, delegation is important. Without it, there are some problems[^1].

In DDoV, there's no _need_ to delegate your vote; you can always cast your vote yourself. Anyone can delegate their vote(s), and anyone who wants to act as a delegate can have votes delegated to them. This setup admits much more flexibility that traditional elected representatives, while still preserving many of the benefits of elected representatives.

The flexibility arises because any individual or group can, hopefully without stigma or repercussion, redelegate their votes at any time, or even reclaim them and cast them manually. A benefit that is preserved is the possibility of centralized decision making. A small number of people _can_, at the behest of the stakeholders, hold majority voting power for particular issues. In these scenarios, a concentrated number of voices can discuss issues and reach compromises. If any compromise is objectionable to the stakeholders, they are at liberty to redelegate their votes, but the possibility for mental offloading to representatives remains.

What is being offloaded to representatives? It's the hard work of understanding the issues being voted on, deciding on the best course of action, convincing others of their opinions, and casting their votes.

Searching around a bit for existing DAOs, I see that voting delegation has been proposed and tried now. I haven't seen any DAO fully implement the DDoV proposal though, allowing for delegating and redelegating. Specifically, here is what I would want to see minimally in an implementation:

1. For each election, every member of an organization receives tokens that represent their voting power. For each token you hold, you can place a vote.
2. Any member can mark themselves as a delegate; this means they can receive tokens from other members.
3. Any member can give a token they hold to a delegate. This includes delegates forwarding tokens they receive to other delegates.
4. A member can recall their tokens back from whoever holds them at any time.

On top of these basic primitives, the following would make the system more useful:

1. Members can set up rules to automatically give out tokens conditioned on the particular issue being voted on. For example, for all education issues, I might automatically send my voting tokens to someone I trust on education.
2. Votes by delegates are made public and locked in before the voting period ends. After this lock-in point, members can still recall their own tokens and modify their own votes. Only delegate-votes cannot be changed (but they can be recalled by the original owner of the voting token.)

Point 1 here allows for effective representatives to emerge, even if in practice they are ephemeral and can have their power revoked by the people at any time.
Point 2 here allows the members to hole ultimate control over their own votes if for some reason their representative behaves in a way contrary to their own views.

I am not yet caught up to date with the implementations that DAOs have tried in practice. This is something I'm interested to learn more about, and then perhaps DDoV (or some future version of it) will be an effective voting strategy for a future DAO.


[^1]: What are the problems that arise with naive voting?
<br/>
(1) You can only hold votes on a small number of things before overwhelming the governing body. If you have too many things to vote on, people will be unable to adequately inform themselves about all items.
<br/>
(2) Everybody needs to learn about and vote on every item.
<br/>
(3) If only a small fraction of voters are voting on typical items, a small number of people could easily sneak a vote past the majority that the majority would disagree with.
