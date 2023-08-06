Action Provider Tools
=====================

This is an experimental and unsupported toolkit to help developers build Action Providers for use in Globus Automate Flows.

As this is experimental, no support is implied or provided for any sort of use of this package. It is published for ease of distribution among those planning to use it for its intended, experimental, purpose.


Toolkit Components
------------------

This toolkit provides two main components:

1. Authentication helpers that make it easier to validate Globus Auth tokens and determine if a given request should be authorized

2. An `OpenAPI v3 specification <http://spec.openapis.org/oas/v3.0.2>`_ and associated helpers that can be used to validate incoming requests and verify the responses your Action Provider generates. This document also defines the interface which must be supported by your REST API to have it function as an Action Provider.


Installation
------------

Installation is via PyPi using, for example: ``pip install globus-action-provider-tools``.


Usage
-----


Authentication
---------------

The authentication helpers can be used in your action provider as follows:

.. code-block:: python

    from globus_action_provider_tools.authentication import TokenChecker
    # You will need to register a client and scope(s) in Globus Auth
    # Then initialize a TokenChecker instance for your provider:
    checker = TokenChecker(
        client_id='YOUR_CLIENT_ID',
        client_secret='YOUR_CLIENT_SECRET',
        expected_scopes=['https://auth.globus.org/scopes/YOUR_SCOPES_HERE'],
        expected_audience='YOUR_CLIENT_NAME',
    )


(expected_audience should be unnecessary in the near future)

When a request comes in, use your TokenChecker to validate the access token from the HTTP Authorization header.

.. code-block:: python

    access_token = request.headers['Authorization'].replace('Bearer ', '')
    auth_state = checker.check_token(access_token)


The AuthState has several properties and methods that will make it easier for you to decide whether or not to allow a request to proceed:

.. code-block:: python

    # This user's Globus identities:
    auth_state.identities
    # frozenset({'urn:globus:auth:identity:9d437146-f150-42c2-be88-9d625d9e7cf9',
    #           'urn:globus:auth:identity:c38f015b-8ad9-4004-9160-754b309b5b33',
    #           'urn:globus:auth:identity:ffb5652b-d418-4849-9b57-556656706970'})
    # Groups this user is a member of:
    auth_state.groups
    # frozenset({'urn:globus:groups:id:606dbaa9-3d57-44b8-a33e-422a9de0c712',
    #           'urn:globus:groups:id:d2ff42bc-c708-460f-9e9b-b535c3776bdd'})


You'll notice that both groups and identities are represented as strings that unambiguously signal what type of entity they represent. This makes it easy to merge the two sets without conflict, for situations where you'd like to work with a single set containing all authentications:

.. code-block:: python

    all_principals = auth_state.identities.union(auth_state.groups)


The AuthState object also offers a helper method, `check_authorization()` that is designed to help you test whether a request should be authorized:

.. code-block:: python

    resource_allows = ['urn:globus:auth:identity:c38f015b-8ad9-4004-9160-754b309b5b33']
    auth_state.check_authorization(resource_allows)
    # True


This method also accepts two special string values, ``'public'`` and ``'all_authenticated_users'``, together with keyword arguments that enable their use:

.. code-block:: python

    resource_allows = ['public']
    auth_state.check_authorization(resource_allows, allow_public=True)
    # True
    resource_allows = ['all_authenticated_users']
    auth_state.check_authorization(resource_allows, allow_all_authenticated_users=True)
   # True


Caching
-------

To avoid excessively taxing Globus Auth, the ``AuthState`` will, by default, cache identities and group memberships for 30 seconds.

The cache is initialized when you first instantiate your ``TokenChecker()``.  You should only need to create one TokenChecker instance for your application, and then you can re-use it to check each new token. If you do try to make multiple instances, you may get an exception:

> ``dogpile.cache.exception.RegionAlreadyConfigured: This region is already configured``

because it's trying to re-initialize a cache that's already been set up.


Validation
----------

There is an OpenAPI v3 specification for the Action Provider API available as described above. You can use any tools that accept OpenAPI v3 to validate requests to and responses from your service, but this toolkit offers some pre-configured validators using the openapi-core library.

.. code-block:: python

    from globus_action_provider_tools.validation import request_validator, response_validator
    # Validating a request
    result = request_validator.validate(request)
    # Or a response:
    result = response_validator.validate(request, response)
    # raise errors if invalid
    result.raise_for_errors()
    # or get list of errors
    errors = result.errors


Note that the ``request`` and ``response`` objects passed to the validators must conform to the `BaseOpenAPI <https://github.com/p1c2u/openapi-core/blob/master/openapi_core/wrappers/base.py>`_ request and response interfaces. If you're using Flask, you can use the `provided wrappers <https://github.com/p1c2u/openapi-core/blob/master/openapi_core/wrappers/flask.py#L10>`_, but if you're using a different web framework, you'll need to write your own small wrapper class.

