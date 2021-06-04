---
mediawiki: How_to_call_a_plugin_with_a_range_of_parameters
title: How to call a plugin with a range of parameters
---

If you want to call a plugin taking a single numerical parameter for a range of values, use a macro like this:

    setBatchMode(true);
    id = getImageID();
    for (radius = 1; radius < 10; radius++) {
        run("Duplicate...", "title=slice");
        run("Gaussian Blur...", "sigma=" + radius);
        run("Select All");
        run("Copy");
        close();
        selectImage(id);
        setSlice(nSlices);
        run("Add Slice");
        run("Paste");
        setSlice(1);
    }
    setBatchMode(false);

This macro takes the current image, and makes a stack of it by adding Gaussian-blurred versions for sigma ("radius") values between *1..9*.

The easiest way to adjust this macro to your needs is to use the Macro Recorder to record one processing step and adjust the recorded call accordingly. For example, a call like **run("Median...", "radius=2");** would have to be edited to replace the **2** by a concatenation of the variable **radius**, i.e. **run("Median...", "radius=" + radius);**.

Note: you might need to call **close();** twice if the plugin you are calling processes images not in place, but rather opens a new image.


