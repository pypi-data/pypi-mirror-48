Factor Analysis
===============

```python

import tensorflow as tf

f = factor_analysis.factors.Factor(data, factor_analysis.posterior.Posterior(covariance_prior, means))

noise = factor_analysis.noise.Noise(f, f.posterior)

with tf.Session() as sess:
    print(f.create_factor().eval())
    print(noise.create_noise(f.create_factor()).eval())
```

