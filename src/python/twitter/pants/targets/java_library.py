# ==================================================================================================
# Copyright 2011 Twitter, Inc.
# --------------------------------------------------------------------------------------------------
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this work except in compliance with the License.
# You may obtain a copy of the License in the LICENSE file, or at:
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==================================================================================================

from .exportable_jvm_library import ExportableJvmLibrary
from .resources import WithLegacyResources


class JavaLibrary(ExportableJvmLibrary, WithLegacyResources):
  """Defines a target that produces a java library."""

  def __init__(self, name, sources=None, provides=None, dependencies=None, excludes=None,
               resources=None, deployjar=False, buildflags=None, exclusives=None):

    """name: The name of this module target, addressable via pants via the portion of the spec
        following the colon
    sources: A list of paths containing the java source files this modules jar is compiled from
    provides: An optional Dependency object indicating the The ivy artifact to export
    dependencies: An optional list of Dependency objects specifying the binary (jar) dependencies of
        this module.
    excludes: An optional list of dependency exclude patterns to filter all of this module's
        transitive dependencies against.
    resources: An optional list of paths containing (filterable) text file resources to place in
        this module's jar
    deployjar: DEPRECATED - An optional boolean that turns on generation of a monolithic deploy
        jar - now ignored.
    buildflags: DEPRECATED - A list of additional command line arguments to pass to the underlying
        build system for this target - now ignored.
    exclusives:   An optional map of exclusives tags. See CheckExclusives for details.
    """

    ExportableJvmLibrary.__init__(self, name, sources, provides, dependencies, excludes, exclusives=exclusives)
    WithLegacyResources.__init__(self, name, sources=sources, resources=resources)

    self.add_labels('java')
