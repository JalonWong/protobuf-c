load("//build-bazel:base.bzl", "VER", "gen_data", "protobuf_c_library", "protobuf_cc_library")

package(default_visibility = ["//visibility:public"])

protobuf_c_library(
    name = "test-proto3_proto",
    srcs = ["test-proto3.proto"],
)

protobuf_c_library(
    name = "test_proto",
    srcs = ["test.proto"],
)

protobuf_c_library(
    name = "test-optimized_proto",
    srcs = ["test-optimized.proto"],
)

protobuf_c_library(
    name = "test-full_proto",
    srcs = ["test-full.proto"],
)

protobuf_cc_library(
    name = "test-full_cc_proto",
    srcs = ["test-full.proto"],
    deps = ["//:protobuf-c_cc_proto"],
)

cc_test(
    name = "test-generated-code_v3",
    srcs = ["generated-code/test-generated-code.c"],
    defines = ["PROTO3"],
    deps = [":test-proto3_proto"],
)

cc_test(
    name = "test-generated-code",
    srcs = ["generated-code/test-generated-code.c"],
    deps = [":test_proto"],
)

cc_test(
    name = "test-version",
    srcs = ["version/version.c"],
    defines = ['PACKAGE_VERSION=\\"' + VER + '\\"'],
    deps = ["//:protobuf-c-inner"],
)

cc_binary(
    name = "cxx-generate-packed-data",
    srcs = ["generated-code2/cxx-generate-packed-data.cc"],
    deps = ["test-full_cc_proto"],
)

gen_data(
    name = "generated-code2-data",
    out = "generated-code2/test-full-cxx-output.inc",
    exe = ":cxx-generate-packed-data",
)

cc_test(
    name = "test-generated-code2",
    srcs = [
        "generated-code2/test-generated-code2.c",
        ":generated-code2-data",
    ],
    deps = [
        ":test-full_proto",
        ":test-optimized_proto",
    ],
)
