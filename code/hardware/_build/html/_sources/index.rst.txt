.. IoT Libraries documentation master file, created by
   sphinx-quickstart on Fri Apr 13 17:34:00 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PiB Python Libraries
=========================================

The following classes are available to students and hobbyists completing a Project in a Box project. They provide examples and enumerate the functions for each hardware device used in our projects. In the content of each project, you are asked to write scripts that interact with circuits, often to save or display readings. We provide these libraries to help you interface with hardware to fulfill those tasks.

In your driver scripts, import these libraries with the following line, replacing DHT22 with the sensor you need:

.. code-block:: python
	
	from libraries.DHT22 import DHT22

.. toctree::
   :maxdepth: 5


MCP300X
=========================================

.. automodule:: MCP300X
.. autoclass:: MCP300X
    :members:
    :inherited-members:
    :show-inheritance:


Sound Detector
=========================================

.. automodule:: Sound_Detector
.. autoclass:: Sound_Detector
    :members:
    :inherited-members:
    :show-inheritance:


DHT22
=========================================

.. automodule:: DHT22
.. autoclass:: DHT22
    :members:
    :inherited-members:
    :show-inheritance:


SSD1306
=========================================

.. automodule:: SSD1306
.. autoclass:: SSD1306.SSD1306_128_32
    :members:
    :inherited-members:
    :show-inheritance:

SSD1306 Demonstration
-----------------------------------------

.. automodule:: SSD1306.test_SSD1306_stats


RGB LED
=========================================

.. automodule:: RGB_LED
.. autoclass:: RGB_LED
    :members:
    :inherited-members:
    :show-inheritance:

Color
-----------------------------------------

.. automodule:: RGB_LED.Color
.. autoclass:: RGB_LED.Color
    :members:
    :inherited-members:
    :show-inheritance:

