package(default_visibility = ["//visibility:private"])

licenses(["notice"])

py_test(
    name = "canonical_form_test",
    size = "large",
    srcs = ["canonical_form_test.py"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        "//tensorflow_federated",
        "//tensorflow_federated/python/common_libs:structure",
        "//tensorflow_federated/python/common_libs:test",
    ],
)

py_test(
    name = "dataset_test",
    size = "small",
    srcs = ["dataset_test.py"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        "//tensorflow_federated",
        "//tensorflow_federated/python/common_libs:test",
    ],
)

py_test(
    name = "perf_regression_test",
    size = "medium",
    srcs = ["perf_regression_test.py"],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = ["//tensorflow_federated"],
)
