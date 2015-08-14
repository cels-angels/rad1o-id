# rad1o-id

Harnessing the awesome power of the cyberspectrum and the rad1o badge

## Purpose

This project has the purpose the of showcasing the fact that you can do arbitrary stuff if you have an SDR frontend.

The idea is that two people meet, bring their rad1os into proximity and exchange a virtual business card.

## Architecture

Development happens in multiple steps:

1. Software implementation of both sides of the transaction in GNU Radio
2. Porting of the transmitter side to rad1o firmware
3. If that makes sense later on, porting of the receiver side, too. 

## Theory

*specific* words might be worth reading up on Wikipedia if you don't know what
they mean.

This is *software defined radio*. So you can't just send bits to the transmit
antenna and hope that they trickle out of the receiver antenna; that's not how
physics works.

So what happens is that you take the input (vCard file) and map the bits to
*complex numbers*; these then go through *pulse shaping*, to give you a
*digital complex baseband signal*. That's what the *DAC* on the rad1o can
convert to an analog I/Q baseband signal and what the frontend chip can
*mix*/*upconvert* (*direct conversion*) to the *RF bandpass signal*, which gets
amplified and sent to the antenna.

On the receiver, the signal coming from the antenna goes through the
*downconverter* and then the *ADC*, which gives us complex digital baseband
again.  Feeding that to a *filter* that is the time-inverse of the TX pulse
shape *FIR filter* eliminates a lot of *noise*, so the *SNR* is maximized. This
is called *matched filtering*.

Now we again have stream of complex numbers. These are related, but not the
same as the transmitted complex numbers: Since we don't know the time the RF
signal was "in flight" and also not the offset between the oscillators used in
mixing or the timing offset between the DAC and ADC, there is a unknown *phase*
offset. But that is nothing more than a complex constant multiplied (`exp(j*2pi
phi)`). So we either need some way of measuring that, or we need a
mapping/demapping from complex numbers to bits that is invariant to phase
shifts. We choose the latter, by using differential encoding, where only the
difference of the *argument of the complex numbers* matters. Hurray!

To let the receiver know that a transmission starts, we need to prepend our
data with a *preamble*, and look for that on the receiver. That inherently
gives our transmission a packet structure. Now, if we do the preamble anyway,
we can also add a length field right after the preamble, and a *CRC* for the
data. Now, that's what you'd usually call a header :)

