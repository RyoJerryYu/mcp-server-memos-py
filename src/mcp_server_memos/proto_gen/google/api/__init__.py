# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: google/api/annotations.proto, google/api/client.proto, google/api/field_behavior.proto, google/api/http.proto, google/api/httpbody.proto, google/api/launch_stage.proto
# plugin: python-betterproto
# This file has been @generated
import warnings
from dataclasses import dataclass
from datetime import timedelta
from typing import (
    Dict,
    List,
)

import betterproto
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf


class LaunchStage(betterproto.Enum):
    """
    The launch stage as defined by [Google Cloud Platform
     Launch Stages](https://cloud.google.com/terms/launch-stages).
    """

    UNSPECIFIED = 0
    """Do not use this default value."""

    UNIMPLEMENTED = 6
    """The feature is not yet implemented. Users can not use it."""

    PRELAUNCH = 7
    """
    Prelaunch features are hidden from users and are only visible internally.
    """

    EARLY_ACCESS = 1
    """
    Early Access features are limited to a closed group of testers. To use
     these features, you must sign up in advance and sign a Trusted Tester
     agreement (which includes confidentiality provisions). These features may
     be unstable, changed in backward-incompatible ways, and are not
     guaranteed to be released.
    """

    ALPHA = 2
    """
    Alpha is a limited availability test for releases before they are cleared
     for widespread use. By Alpha, all significant design issues are resolved
     and we are in the process of verifying functionality. Alpha customers
     need to apply for access, agree to applicable terms, and have their
     projects allowlisted. Alpha releases don't have to be feature complete,
     no SLAs are provided, and there are no technical support obligations, but
     they will be far enough along that customers can actually use them in
     test environments or for limited-use tests -- just like they would in
     normal production cases.
    """

    BETA = 3
    """
    Beta is the point at which we are ready to open a release for any
     customer to use. There are no SLA or technical support obligations in a
     Beta release. Products will be complete from a feature perspective, but
     may have some open outstanding issues. Beta releases are suitable for
     limited production use cases.
    """

    GA = 4
    """
    GA features are open to all developers and are considered stable and
     fully qualified for production use.
    """

    DEPRECATED = 5
    """
    Deprecated features are scheduled to be shut down and removed. For more
     information, see the "Deprecation Policy" section of our [Terms of
     Service](https://cloud.google.com/terms/)
     and the [Google Cloud Platform Subject to the Deprecation
     Policy](https://cloud.google.com/terms/deprecation) documentation.
    """


class ClientLibraryOrganization(betterproto.Enum):
    """
    The organization for which the client libraries are being published.
     Affects the url where generated docs are published, etc.
    """

    UNSPECIFIED = 0
    """Not useful."""

    CLOUD = 1
    """Google Cloud Platform Org."""

    ADS = 2
    """Ads (Advertising) Org."""

    PHOTOS = 3
    """Photos Org."""

    STREET_VIEW = 4
    """Street View Org."""

    SHOPPING = 5
    """Shopping Org."""

    GEO = 6
    """Geo Org."""

    GENERATIVE_AI = 7
    """Generative AI - https://developers.generativeai.google"""


class ClientLibraryDestination(betterproto.Enum):
    """To where should client libraries be published?"""

    UNSPECIFIED = 0
    """
    Client libraries will neither be generated nor published to package
     managers.
    """

    GITHUB = 10
    """
    Generate the client library in a repo under github.com/googleapis,
     but don't publish it to package managers.
    """

    PACKAGE_MANAGER = 20
    """
    Publish the library to package managers like nuget.org and npmjs.com.
    """


class FieldBehavior(betterproto.Enum):
    """
    An indicator of the behavior of a given field (for example, that a field
     is required in requests, or given as output but ignored as input).
     This **does not** change the behavior in protocol buffers itself; it only
     denotes the behavior and may affect how API tooling handles the field.

     Note: This enum **may** receive new values in the future.
    """

    UNSPECIFIED = 0
    """Conventional default for enums. Do not use this."""

    OPTIONAL = 1
    """
    Specifically denotes a field as optional.
     While all fields in protocol buffers are optional, this may be specified
     for emphasis if appropriate.
    """

    REQUIRED = 2
    """
    Denotes a field as required.
     This indicates that the field **must** be provided as part of the request,
     and failure to do so will cause an error (usually `INVALID_ARGUMENT`).
    """

    OUTPUT_ONLY = 3
    """
    Denotes a field as output only.
     This indicates that the field is provided in responses, but including the
     field in a request does nothing (the server *must* ignore it and
     *must not* throw an error as a result of the field's presence).
    """

    INPUT_ONLY = 4
    """
    Denotes a field as input only.
     This indicates that the field is provided in requests, and the
     corresponding field is not included in output.
    """

    IMMUTABLE = 5
    """
    Denotes a field as immutable.
     This indicates that the field may be set once in a request to create a
     resource, but may not be changed thereafter.
    """

    UNORDERED_LIST = 6
    """
    Denotes that a (repeated) field is an unordered list.
     This indicates that the service may provide the elements of the list
     in any arbitrary  order, rather than the order the user originally
     provided. Additionally, the list's order may or may not be stable.
    """

    NON_EMPTY_DEFAULT = 7
    """
    Denotes that this field returns a non-empty default value if not set.
     This indicates that if the user provides the empty value in a request,
     a non-empty value will be returned. The user will not be aware of what
     non-empty value to expect.
    """

    IDENTIFIER = 8
    """
    Denotes that the field in a resource (a message annotated with
     google.api.resource) is used in the resource name to uniquely identify the
     resource. For AIP-compliant APIs, this should only be applied to the
     `name` field on the resource.
    
     This behavior should not be applied to references to other resources within
     the message.
    
     The identifier field of resources often have different field behavior
     depending on the request it is embedded in (e.g. for Create methods name
     is optional and unused, while for Update methods it is required). Instead
     of method-specific annotations, only `IDENTIFIER` is required.
    """


@dataclass(eq=False, repr=False)
class Http(betterproto.Message):
    """
    Defines the HTTP configuration for an API service. It contains a list of
     [HttpRule][google.api.HttpRule], each specifying the mapping of an RPC method
     to one or more HTTP REST API methods.
    """

    rules: List["HttpRule"] = betterproto.message_field(1)
    """
    A list of HTTP configuration rules that apply to individual API methods.
    
     **NOTE:** All service configuration rules follow "last one wins" order.
    """

    fully_decode_reserved_expansion: bool = betterproto.bool_field(2)
    """
    When set to true, URL path parameters will be fully URI-decoded except in
     cases of single segment matches in reserved expansion, where "%2F" will be
     left encoded.
    
     The default behavior is to not decode RFC 6570 reserved characters in multi
     segment matches.
    """


@dataclass(eq=False, repr=False)
class HttpRule(betterproto.Message):
    """
    gRPC Transcoding

     gRPC Transcoding is a feature for mapping between a gRPC method and one or
     more HTTP REST endpoints. It allows developers to build a single API service
     that supports both gRPC APIs and REST APIs. Many systems, including [Google
     APIs](https://github.com/googleapis/googleapis),
     [Cloud Endpoints](https://cloud.google.com/endpoints), [gRPC
     Gateway](https://github.com/grpc-ecosystem/grpc-gateway),
     and [Envoy](https://github.com/envoyproxy/envoy) proxy support this feature
     and use it for large scale production services.

     `HttpRule` defines the schema of the gRPC/REST mapping. The mapping specifies
     how different portions of the gRPC request message are mapped to the URL
     path, URL query parameters, and HTTP request body. It also controls how the
     gRPC response message is mapped to the HTTP response body. `HttpRule` is
     typically specified as an `google.api.http` annotation on the gRPC method.

     Each mapping specifies a URL path template and an HTTP method. The path
     template may refer to one or more fields in the gRPC request message, as long
     as each field is a non-repeated field with a primitive (non-message) type.
     The path template controls how fields of the request message are mapped to
     the URL path.

     Example:

         service Messaging {
           rpc GetMessage(GetMessageRequest) returns (Message) {
             option (google.api.http) = {
                 get: "/v1/{name=messages/*}"
             };
           }
         }
         message GetMessageRequest {
           string name = 1; // Mapped to URL path.
         }
         message Message {
           string text = 1; // The resource content.
         }

     This enables an HTTP REST to gRPC mapping as below:

     - HTTP: `GET /v1/messages/123456`
     - gRPC: `GetMessage(name: "messages/123456")`

     Any fields in the request message which are not bound by the path template
     automatically become HTTP query parameters if there is no HTTP request body.
     For example:

         service Messaging {
           rpc GetMessage(GetMessageRequest) returns (Message) {
             option (google.api.http) = {
                 get:"/v1/messages/{message_id}"
             };
           }
         }
         message GetMessageRequest {
           message SubMessage {
             string subfield = 1;
           }
           string message_id = 1; // Mapped to URL path.
           int64 revision = 2;    // Mapped to URL query parameter `revision`.
           SubMessage sub = 3;    // Mapped to URL query parameter `sub.subfield`.
         }

     This enables a HTTP JSON to RPC mapping as below:

     - HTTP: `GET /v1/messages/123456?revision=2&sub.subfield=foo`
     - gRPC: `GetMessage(message_id: "123456" revision: 2 sub:
     SubMessage(subfield: "foo"))`

     Note that fields which are mapped to URL query parameters must have a
     primitive type or a repeated primitive type or a non-repeated message type.
     In the case of a repeated type, the parameter can be repeated in the URL
     as `...?param=A&param=B`. In the case of a message type, each field of the
     message is mapped to a separate parameter, such as
     `...?foo.a=A&foo.b=B&foo.c=C`.

     For HTTP methods that allow a request body, the `body` field
     specifies the mapping. Consider a REST update method on the
     message resource collection:

         service Messaging {
           rpc UpdateMessage(UpdateMessageRequest) returns (Message) {
             option (google.api.http) = {
               patch: "/v1/messages/{message_id}"
               body: "message"
             };
           }
         }
         message UpdateMessageRequest {
           string message_id = 1; // mapped to the URL
           Message message = 2;   // mapped to the body
         }

     The following HTTP JSON to RPC mapping is enabled, where the
     representation of the JSON in the request body is determined by
     protos JSON encoding:

     - HTTP: `PATCH /v1/messages/123456 { "text": "Hi!" }`
     - gRPC: `UpdateMessage(message_id: "123456" message { text: "Hi!" })`

     The special name `*` can be used in the body mapping to define that
     every field not bound by the path template should be mapped to the
     request body.  This enables the following alternative definition of
     the update method:

         service Messaging {
           rpc UpdateMessage(Message) returns (Message) {
             option (google.api.http) = {
               patch: "/v1/messages/{message_id}"
               body: "*"
             };
           }
         }
         message Message {
           string message_id = 1;
           string text = 2;
         }


     The following HTTP JSON to RPC mapping is enabled:

     - HTTP: `PATCH /v1/messages/123456 { "text": "Hi!" }`
     - gRPC: `UpdateMessage(message_id: "123456" text: "Hi!")`

     Note that when using `*` in the body mapping, it is not possible to
     have HTTP parameters, as all fields not bound by the path end in
     the body. This makes this option more rarely used in practice when
     defining REST APIs. The common usage of `*` is in custom methods
     which don't use the URL at all for transferring data.

     It is possible to define multiple HTTP methods for one RPC by using
     the `additional_bindings` option. Example:

         service Messaging {
           rpc GetMessage(GetMessageRequest) returns (Message) {
             option (google.api.http) = {
               get: "/v1/messages/{message_id}"
               additional_bindings {
                 get: "/v1/users/{user_id}/messages/{message_id}"
               }
             };
           }
         }
         message GetMessageRequest {
           string message_id = 1;
           string user_id = 2;
         }

     This enables the following two alternative HTTP JSON to RPC mappings:

     - HTTP: `GET /v1/messages/123456`
     - gRPC: `GetMessage(message_id: "123456")`

     - HTTP: `GET /v1/users/me/messages/123456`
     - gRPC: `GetMessage(user_id: "me" message_id: "123456")`

     Rules for HTTP mapping

     1. Leaf request fields (recursive expansion nested messages in the request
        message) are classified into three categories:
        - Fields referred by the path template. They are passed via the URL path.
        - Fields referred by the [HttpRule.body][google.api.HttpRule.body]. They
        are passed via the HTTP
          request body.
        - All other fields are passed via the URL query parameters, and the
          parameter name is the field path in the request message. A repeated
          field can be represented as multiple query parameters under the same
          name.
      2. If [HttpRule.body][google.api.HttpRule.body] is "*", there is no URL
      query parameter, all fields
         are passed via URL path and HTTP request body.
      3. If [HttpRule.body][google.api.HttpRule.body] is omitted, there is no HTTP
      request body, all
         fields are passed via URL path and URL query parameters.

     Path template syntax

         Template = "/" Segments [ Verb ] ;
         Segments = Segment { "/" Segment } ;
         Segment  = "*" | "**" | LITERAL | Variable ;
         Variable = "{" FieldPath [ "=" Segments ] "}" ;
         FieldPath = IDENT { "." IDENT } ;
         Verb     = ":" LITERAL ;

     The syntax `*` matches a single URL path segment. The syntax `**` matches
     zero or more URL path segments, which must be the last part of the URL path
     except the `Verb`.

     The syntax `Variable` matches part of the URL path as specified by its
     template. A variable template must not contain other variables. If a variable
     matches a single path segment, its template may be omitted, e.g. `{var}`
     is equivalent to `{var=*}`.

     The syntax `LITERAL` matches literal text in the URL path. If the `LITERAL`
     contains any reserved character, such characters should be percent-encoded
     before the matching.

     If a variable contains exactly one path segment, such as `"{var}"` or
     `"{var=*}"`, when such a variable is expanded into a URL path on the client
     side, all characters except `[-_.~0-9a-zA-Z]` are percent-encoded. The
     server side does the reverse decoding. Such variables show up in the
     [Discovery
     Document](https://developers.google.com/discovery/v1/reference/apis) as
     `{var}`.

     If a variable contains multiple path segments, such as `"{var=foo/*}"`
     or `"{var=**}"`, when such a variable is expanded into a URL path on the
     client side, all characters except `[-_.~/0-9a-zA-Z]` are percent-encoded.
     The server side does the reverse decoding, except "%2F" and "%2f" are left
     unchanged. Such variables show up in the
     [Discovery
     Document](https://developers.google.com/discovery/v1/reference/apis) as
     `{+var}`.

     Using gRPC API Service Configuration

     gRPC API Service Configuration (service config) is a configuration language
     for configuring a gRPC service to become a user-facing product. The
     service config is simply the YAML representation of the `google.api.Service`
     proto message.

     As an alternative to annotating your proto file, you can configure gRPC
     transcoding in your service config YAML files. You do this by specifying a
     `HttpRule` that maps the gRPC method to a REST endpoint, achieving the same
     effect as the proto annotation. This can be particularly useful if you
     have a proto that is reused in multiple services. Note that any transcoding
     specified in the service config will override any matching transcoding
     configuration in the proto.

     The following example selects a gRPC method and applies an `HttpRule` to it:

         http:
           rules:
             - selector: example.v1.Messaging.GetMessage
               get: /v1/messages/{message_id}/{sub.subfield}

     Special notes

     When gRPC Transcoding is used to map a gRPC to JSON REST endpoints, the
     proto to JSON conversion must follow the [proto3
     specification](https://developers.google.com/protocol-buffers/docs/proto3#json).

     While the single segment variable follows the semantics of
     [RFC 6570](https://tools.ietf.org/html/rfc6570) Section 3.2.2 Simple String
     Expansion, the multi segment variable **does not** follow RFC 6570 Section
     3.2.3 Reserved Expansion. The reason is that the Reserved Expansion
     does not expand special characters like `?` and `#`, which would lead
     to invalid URLs. As the result, gRPC Transcoding uses a custom encoding
     for multi segment variables.

     The path variables **must not** refer to any repeated or mapped field,
     because client libraries are not capable of handling such variable expansion.

     The path variables **must not** capture the leading "/" character. The reason
     is that the most common use case "{var}" does not capture the leading "/"
     character. For consistency, all path variables must share the same behavior.

     Repeated message fields must not be mapped to URL query parameters, because
     no client library can support such complicated mapping.

     If an API needs to use a JSON array for request or response body, it can map
     the request or response body to a repeated field. However, some gRPC
     Transcoding implementations may not support this feature.
    """

    selector: str = betterproto.string_field(1)
    """
    Selects a method to which this rule applies.
    
     Refer to [selector][google.api.DocumentationRule.selector] for syntax
     details.
    """

    get: str = betterproto.string_field(2, group="pattern")
    """
    Maps to HTTP GET. Used for listing and getting information about
     resources.
    """

    put: str = betterproto.string_field(3, group="pattern")
    """Maps to HTTP PUT. Used for replacing a resource."""

    post: str = betterproto.string_field(4, group="pattern")
    """
    Maps to HTTP POST. Used for creating a resource or performing an action.
    """

    delete: str = betterproto.string_field(5, group="pattern")
    """Maps to HTTP DELETE. Used for deleting a resource."""

    patch: str = betterproto.string_field(6, group="pattern")
    """Maps to HTTP PATCH. Used for updating a resource."""

    custom: "CustomHttpPattern" = betterproto.message_field(8, group="pattern")
    """
    The custom pattern is used for specifying an HTTP method that is not
     included in the `pattern` field, such as HEAD, or "*" to leave the
     HTTP method unspecified for this rule. The wild-card rule is useful
     for services that provide content to Web (HTML) clients.
    """

    body: str = betterproto.string_field(7)
    """
    The name of the request field whose value is mapped to the HTTP request
     body, or `*` for mapping all request fields not captured by the path
     pattern to the HTTP body, or omitted for not having any HTTP request body.
    
     NOTE: the referred field must be present at the top-level of the request
     message type.
    """

    response_body: str = betterproto.string_field(12)
    """
    Optional. The name of the response field whose value is mapped to the HTTP
     response body. When omitted, the entire response message will be used
     as the HTTP response body.
    
     NOTE: The referred field must be present at the top-level of the response
     message type.
    """

    additional_bindings: List["HttpRule"] = betterproto.message_field(11)
    """
    Additional HTTP bindings for the selector. Nested bindings must
     not contain an `additional_bindings` field themselves (that is,
     the nesting may only be one level deep).
    """


@dataclass(eq=False, repr=False)
class CustomHttpPattern(betterproto.Message):
    """A custom pattern is used for defining custom HTTP verb."""

    kind: str = betterproto.string_field(1)
    """The name of this custom HTTP verb."""

    path: str = betterproto.string_field(2)
    """The path matched by this custom verb."""


@dataclass(eq=False, repr=False)
class CommonLanguageSettings(betterproto.Message):
    """Required information for every language."""

    reference_docs_uri: str = betterproto.string_field(1)
    """
    Link to automatically generated reference documentation.  Example:
     https://cloud.google.com/nodejs/docs/reference/asset/latest
    """

    destinations: List["ClientLibraryDestination"] = betterproto.enum_field(2)
    """
    The destination where API teams want this client library to be published.
    """

    selective_gapic_generation: "SelectiveGapicGeneration" = betterproto.message_field(
        3
    )
    """
    Configuration for which RPCs should be generated in the GAPIC client.
    """

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.is_set("reference_docs_uri"):
            warnings.warn(
                "CommonLanguageSettings.reference_docs_uri is deprecated",
                DeprecationWarning,
            )


@dataclass(eq=False, repr=False)
class ClientLibrarySettings(betterproto.Message):
    """Details about how and where to publish client libraries."""

    version: str = betterproto.string_field(1)
    """
    Version of the API to apply these settings to. This is the full protobuf
     package for the API, ending in the version element.
     Examples: "google.cloud.speech.v1" and "google.spanner.admin.database.v1".
    """

    launch_stage: "LaunchStage" = betterproto.enum_field(2)
    """Launch stage of this version of the API."""

    rest_numeric_enums: bool = betterproto.bool_field(3)
    """
    When using transport=rest, the client request will encode enums as
     numbers rather than strings.
    """

    java_settings: "JavaSettings" = betterproto.message_field(21)
    """Settings for legacy Java features, supported in the Service YAML."""

    cpp_settings: "CppSettings" = betterproto.message_field(22)
    """Settings for C++ client libraries."""

    php_settings: "PhpSettings" = betterproto.message_field(23)
    """Settings for PHP client libraries."""

    python_settings: "PythonSettings" = betterproto.message_field(24)
    """Settings for Python client libraries."""

    node_settings: "NodeSettings" = betterproto.message_field(25)
    """Settings for Node client libraries."""

    dotnet_settings: "DotnetSettings" = betterproto.message_field(26)
    """Settings for .NET client libraries."""

    ruby_settings: "RubySettings" = betterproto.message_field(27)
    """Settings for Ruby client libraries."""

    go_settings: "GoSettings" = betterproto.message_field(28)
    """Settings for Go client libraries."""


@dataclass(eq=False, repr=False)
class Publishing(betterproto.Message):
    """
    This message configures the settings for publishing [Google Cloud Client
     libraries](https://cloud.google.com/apis/docs/cloud-client-libraries)
     generated from the service config.
    """

    method_settings: List["MethodSettings"] = betterproto.message_field(2)
    """
    A list of API method settings, e.g. the behavior for methods that use the
     long-running operation pattern.
    """

    new_issue_uri: str = betterproto.string_field(101)
    """
    Link to a *public* URI where users can report issues.  Example:
     https://issuetracker.google.com/issues/new?component=190865&template=1161103
    """

    documentation_uri: str = betterproto.string_field(102)
    """
    Link to product home page.  Example:
     https://cloud.google.com/asset-inventory/docs/overview
    """

    api_short_name: str = betterproto.string_field(103)
    """
    Used as a tracking tag when collecting data about the APIs developer
     relations artifacts like docs, packages delivered to package managers,
     etc.  Example: "speech".
    """

    github_label: str = betterproto.string_field(104)
    """
    GitHub label to apply to issues and pull requests opened for this API.
    """

    codeowner_github_teams: List[str] = betterproto.string_field(105)
    """
    GitHub teams to be added to CODEOWNERS in the directory in GitHub
     containing source code for the client libraries for this API.
    """

    doc_tag_prefix: str = betterproto.string_field(106)
    """
    A prefix used in sample code when demarking regions to be included in
     documentation.
    """

    organization: "ClientLibraryOrganization" = betterproto.enum_field(107)
    """For whom the client library is being published."""

    library_settings: List["ClientLibrarySettings"] = betterproto.message_field(109)
    """
    Client library settings.  If the same version string appears multiple
     times in this list, then the last one wins.  Settings from earlier
     settings with the same version string are discarded.
    """

    proto_reference_documentation_uri: str = betterproto.string_field(110)
    """
    Optional link to proto reference documentation.  Example:
     https://cloud.google.com/pubsub/lite/docs/reference/rpc
    """

    rest_reference_documentation_uri: str = betterproto.string_field(111)
    """
    Optional link to REST reference documentation.  Example:
     https://cloud.google.com/pubsub/lite/docs/reference/rest
    """


@dataclass(eq=False, repr=False)
class JavaSettings(betterproto.Message):
    """Settings for Java client libraries."""

    library_package: str = betterproto.string_field(1)
    """
    The package name to use in Java. Clobbers the java_package option
     set in the protobuf. This should be used **only** by APIs
     who have already set the language_settings.java.package_name" field
     in gapic.yaml. API teams should use the protobuf java_package option
     where possible.
    
     Example of a YAML configuration::
    
      publishing:
        java_settings:
          library_package: com.google.cloud.pubsub.v1
    """

    service_class_names: Dict[str, str] = betterproto.map_field(
        2, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )
    """
    Configure the Java class name to use instead of the service's for its
     corresponding generated GAPIC client. Keys are fully-qualified
     service names as they appear in the protobuf (including the full
     the language_settings.java.interface_names" field in gapic.yaml. API
     teams should otherwise use the service name as it appears in the
     protobuf.
    
     Example of a YAML configuration::
    
      publishing:
        java_settings:
          service_class_names:
            - google.pubsub.v1.Publisher: TopicAdmin
            - google.pubsub.v1.Subscriber: SubscriptionAdmin
    """

    common: "CommonLanguageSettings" = betterproto.message_field(3)
    """Some settings."""


@dataclass(eq=False, repr=False)
class CppSettings(betterproto.Message):
    """Settings for C++ client libraries."""

    common: "CommonLanguageSettings" = betterproto.message_field(1)
    """Some settings."""


@dataclass(eq=False, repr=False)
class PhpSettings(betterproto.Message):
    """Settings for Php client libraries."""

    common: "CommonLanguageSettings" = betterproto.message_field(1)
    """Some settings."""


@dataclass(eq=False, repr=False)
class PythonSettings(betterproto.Message):
    """Settings for Python client libraries."""

    common: "CommonLanguageSettings" = betterproto.message_field(1)
    """Some settings."""

    experimental_features: "PythonSettingsExperimentalFeatures" = (
        betterproto.message_field(2)
    )
    """
    Experimental features to be included during client library generation.
    """


@dataclass(eq=False, repr=False)
class PythonSettingsExperimentalFeatures(betterproto.Message):
    """
    Experimental features to be included during client library generation.
     These fields will be deprecated once the feature graduates and is enabled
     by default.
    """

    rest_async_io_enabled: bool = betterproto.bool_field(1)
    """
    Enables generation of asynchronous REST clients if `rest` transport is
     enabled. By default, asynchronous REST clients will not be generated.
     This feature will be enabled by default 1 month after launching the
     feature in preview packages.
    """

    protobuf_pythonic_types_enabled: bool = betterproto.bool_field(2)
    """
    Enables generation of protobuf code using new types that are more
     Pythonic which are included in `protobuf>=5.29.x`. This feature will be
     enabled by default 1 month after launching the feature in preview
     packages.
    """


@dataclass(eq=False, repr=False)
class NodeSettings(betterproto.Message):
    """Settings for Node client libraries."""

    common: "CommonLanguageSettings" = betterproto.message_field(1)
    """Some settings."""


@dataclass(eq=False, repr=False)
class DotnetSettings(betterproto.Message):
    """Settings for Dotnet client libraries."""

    common: "CommonLanguageSettings" = betterproto.message_field(1)
    """Some settings."""

    renamed_services: Dict[str, str] = betterproto.map_field(
        2, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )
    """
    Map from original service names to renamed versions.
     This is used when the default generated types
     would cause a naming conflict. (Neither name is
     fully-qualified.)
     Example: Subscriber to SubscriberServiceApi.
    """

    renamed_resources: Dict[str, str] = betterproto.map_field(
        3, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )
    """
    Map from full resource types to the effective short name
     for the resource. This is used when otherwise resource
     named from different services would cause naming collisions.
     Example entry:
     "datalabeling.googleapis.com/Dataset": "DataLabelingDataset"
    """

    ignored_resources: List[str] = betterproto.string_field(4)
    """
    List of full resource types to ignore during generation.
     This is typically used for API-specific Location resources,
     which should be handled by the generator as if they were actually
     the common Location resources.
     Example entry: "documentai.googleapis.com/Location"
    """

    forced_namespace_aliases: List[str] = betterproto.string_field(5)
    """
    Namespaces which must be aliased in snippets due to
     a known (but non-generator-predictable) naming collision
    """

    handwritten_signatures: List[str] = betterproto.string_field(6)
    """
    Method signatures (in the form "service.method(signature)")
     which are provided separately, so shouldn't be generated.
     Snippets *calling* these methods are still generated, however.
    """


@dataclass(eq=False, repr=False)
class RubySettings(betterproto.Message):
    """Settings for Ruby client libraries."""

    common: "CommonLanguageSettings" = betterproto.message_field(1)
    """Some settings."""


@dataclass(eq=False, repr=False)
class GoSettings(betterproto.Message):
    """Settings for Go client libraries."""

    common: "CommonLanguageSettings" = betterproto.message_field(1)
    """Some settings."""

    renamed_services: Dict[str, str] = betterproto.map_field(
        2, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )
    """
    Map of service names to renamed services. Keys are the package relative
     service names and values are the name to be used for the service client
     and call options.
    
     publishing:
       go_settings:
         renamed_services:
           Publisher: TopicAdmin
    """


@dataclass(eq=False, repr=False)
class MethodSettings(betterproto.Message):
    """Describes the generator configuration for a method."""

    selector: str = betterproto.string_field(1)
    """
    The fully qualified name of the method, for which the options below apply.
     This is used to find the method to apply the options.
    
     Example:
    
        publishing:
          method_settings:
          - selector: google.storage.control.v2.StorageControl.CreateFolder
            # method settings for CreateFolder...
    """

    long_running: "MethodSettingsLongRunning" = betterproto.message_field(2)
    """
    Describes settings to use for long-running operations when generating
     API methods for RPCs. Complements RPCs that use the annotations in
     google/longrunning/operations.proto.
    
     Example of a YAML configuration::
    
        publishing:
          method_settings:
          - selector: google.cloud.speech.v2.Speech.BatchRecognize
            long_running:
              initial_poll_delay: 60s # 1 minute
              poll_delay_multiplier: 1.5
              max_poll_delay: 360s # 6 minutes
              total_poll_timeout: 54000s # 90 minutes
    """

    auto_populated_fields: List[str] = betterproto.string_field(3)
    """
    List of top-level fields of the request message, that should be
     automatically populated by the client libraries based on their
     (google.api.field_info).format. Currently supported format: UUID4.
    
     Example of a YAML configuration:
    
        publishing:
          method_settings:
          - selector: google.example.v1.ExampleService.CreateExample
            auto_populated_fields:
            - request_id
    """


@dataclass(eq=False, repr=False)
class MethodSettingsLongRunning(betterproto.Message):
    """
    Describes settings to use when generating API methods that use the
     long-running operation pattern.
     All default values below are from those used in the client library
     generators (e.g.
     [Java](https://github.com/googleapis/gapic-generator-java/blob/04c2faa191a9b5a10b92392fe8482279c4404803/src/main/java/com/google/api/generator/gapic/composer/common/RetrySettingsComposer.java)).
    """

    initial_poll_delay: timedelta = betterproto.message_field(1)
    """
    Initial delay after which the first poll request will be made.
     Default value: 5 seconds.
    """

    poll_delay_multiplier: float = betterproto.float_field(2)
    """
    Multiplier to gradually increase delay between subsequent polls until it
     reaches max_poll_delay.
     Default value: 1.5.
    """

    max_poll_delay: timedelta = betterproto.message_field(3)
    """
    Maximum time between two subsequent poll requests.
     Default value: 45 seconds.
    """

    total_poll_timeout: timedelta = betterproto.message_field(4)
    """
    Total polling timeout.
     Default value: 5 minutes.
    """


@dataclass(eq=False, repr=False)
class SelectiveGapicGeneration(betterproto.Message):
    """
    This message is used to configure the generation of a subset of the RPCs in
     a service for client libraries.
    """

    methods: List[str] = betterproto.string_field(1)
    """
    An allowlist of the fully qualified names of RPCs that should be included
     on public client surfaces.
    """


@dataclass(eq=False, repr=False)
class HttpBody(betterproto.Message):
    """
    Message that represents an arbitrary HTTP body. It should only be used for
     payload formats that can't be represented as JSON, such as raw binary or
     an HTML page.


     This message can be used both in streaming and non-streaming API methods in
     the request as well as the response.

     It can be used as a top-level request field, which is convenient if one
     wants to extract parameters from either the URL or HTTP template into the
     request fields and also want access to the raw HTTP body.

     Example:

         message GetResourceRequest {
           // A unique request id.
           string request_id = 1;

           // The raw HTTP body is bound to this field.
           google.api.HttpBody http_body = 2;

         }

         service ResourceService {
           rpc GetResource(GetResourceRequest)
             returns (google.api.HttpBody);
           rpc UpdateResource(google.api.HttpBody)
             returns (google.protobuf.Empty);

         }

     Example with streaming methods:

         service CaldavService {
           rpc GetCalendar(stream google.api.HttpBody)
             returns (stream google.api.HttpBody);
           rpc UpdateCalendar(stream google.api.HttpBody)
             returns (stream google.api.HttpBody);

         }

     Use of this type only changes how the request and response bodies are
     handled, all other features will continue to work unchanged.
    """

    content_type: str = betterproto.string_field(1)
    """
    The HTTP Content-Type header value specifying the content type of the body.
    """

    data: bytes = betterproto.bytes_field(2)
    """The HTTP request/response body as raw binary."""

    extensions: List["betterproto_lib_google_protobuf.Any"] = betterproto.message_field(
        3
    )
    """
    Application specific response metadata. Must be set in the first response
     for streaming APIs.
    """
