# tune2vec

## Motivation

When I worked at a radio station in Chicago I was disappointed to learn nobody listens to music. If you're surrounded by music you simply don't have time to listen to anything. Music is chosen via metadata: artist, title, cover art etc because these can quickly be digested.

What's needed is a music recommendation that's based on the music itself. The first step is to find an embedding for a musical track. Once we have vectors we can do all kinds of cool things like k-Nearest Neighbors to cluster the music. How cool would it be if a machine learning algorithm learned that B.B. King was like Albert King was like Freddie King? Pretty cool, that's what.

## Approach

The straightforward approach is to build an autoencoder:

audio in -> CNN + RNN (encoder) -> RNN + CNN (decoder)-> audio out

error ~ audio in - audio out

