# WhatsOpt Tutorial - Part 3

## Advanced features

### Prerequisite

You are logged in WhatsOpt with <code>wop</code>. See WhatsOpt Tutorial - Part 2

### From source code to WhatsOpt

As we saw in previous parts, we are able to generate OpenMDAO source code from an analysis defined in WhatsOpt. We are going to see that we can do the other way around.

With certain limitations explained below, we can create an analysis in WhatsOpt from an OpenMDAO source code, especially when the later one is originated from WhatsOpt.

The wop command allowing to so is <code>wop push <file.py></code>, where <file.py> is an Python file containing an OpenMDAO Problem setup. To experiment you can use the sellar code in examples directory.

```bash
cd examples/sellar
wop push sellar.py
```

Then you can observe that a new analysis is available in WhatsOpt _Analyses_ page list. This new analysis is a duplicate of the Sellar analysis we built manually in the Part 1 of this tutorial.

Following a top-down approach where the ideal analysis is designed not depending on existing implementations, WhatsOpt main assumption is that variable names are visible globally (i.e. all needed variables are promoted). And indeed, the analysis building process within WhatsOpt ensures that variable names are unique.

<strong>So OpenMDAO code that does not follow that principle will not work. In other words, presence of connections defined with <code>connect</code> will not work.</strong>

### Analysis Server

To be completed...

### Operations Management

To be completed...



```python

```
