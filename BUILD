load("//build-bazel:base.bzl", "VER", "protobuf_cc_library")

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "protobuf-c-inner",
    srcs = ["protobuf-c/protobuf-c.c"],
    hdrs = ["protobuf-c/protobuf-c.h"],
)

cc_shared_library(
    name = "protobuf-c",
    deps = [":protobuf-c-inner"],
)

protobuf_cc_library(
    name = "protobuf-c_cc_proto",
    srcs = ["protobuf-c/protobuf-c.proto"],
    includes = [],
)

cc_binary(
    name = "protoc-gen-c",
    srcs = glob(["protoc-c/*.cc"]),
    defines = ['PACKAGE_VERSION=\\"' + VER + '\\"'],
    includes = ["protoc-c"],
    deps = [
        ":protobuf-c-inner",
        ":protobuf-c_cc_proto",
    ],
)

filegroup(
    name = "all",
    srcs = [
        ":protoc-gen-c",
        ":protobuf-c",
    ],
)

test_suite(
    name = "tests",
    tests = [
        "//t:test-generated-code",
        "//t:test-generated-code2",
        "//t:test-generated-code_v3",
        "//t:test-version",
        "//t/issue204",
        "//t/issue220",
        "//t/issue251",
        "//t/issue330",
        "//t/issue375",
        "//t/issue440",
    ],
)
