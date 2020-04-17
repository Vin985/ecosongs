### Detector evaluation

1. Since we cannot infer the name of an audio file from the annotation filename (we don't know the extension of the file) recordings are loaded from the database using the absolute path found in the annotation file. However, when loading the events, the path is not used, just the file name without extension. This is why before matching events, it is important to remove the extension to select events.

### Analysis options

1. Options are stocked in a single column for simplicity. To expand the options into a new dataframe where each option has its own column, please see the AnalysisOptionsTable.expand_options() method. Note that this function only works if all rows have the same number of options.