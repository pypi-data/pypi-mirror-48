<p align=center>
    <img src="media/logo.png" alt="Delivery Logo" />
</p>

<h1 align=center>Delivery</h1>

<p align=center>Desktop notifications for every platform, in Python.</p>

<p align=center>
:incoming_envelope:
</p>

---

<!-- ## What is this Package? -->

A simple, multiplatform library for desktop notifications.

I wasn't impressed with the existing offerings. This is an attempt to provide a simple interface that really does work on all platforms.

Here's an example:

```python
import delivery

delivery.notify("Urgent Information", "Delivery is great. Install it with pip!")
```

Easy, and stable. Install it with pip:

```shell
pip install delivery
```

Under the hood, most of the work is done by [plyer](https://github.com/kivy/plyer), made by the creators of Kivy.
