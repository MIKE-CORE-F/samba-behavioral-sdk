#include "SANBA_BEHAVIORAL_SDK_GEDRAGS.h"
#include <cstddef>

SANBA_BEHAVIORAL_SDK_GEDRAGS::SANBA_BEHAVIORAL_SDK_GEDRAGS() : gedragsdata_(NULL) {}
SANBA_BEHAVIORAL_SDK_GEDRAGS::~SANBA_BEHAVIORAL_SDK_GEDRAGS() { gedragsdata_ = NULL; }

bool SANBA_BEHAVIORAL_SDK_GEDRAGS::Initialize() { return true; }
bool SANBA_BEHAVIORAL_SDK_GEDRAGS::Licentiecontrole() { return true; }
bool SANBA_BEHAVIORAL_SDK_GEDRAGS::Gebruikerauthenticatie() { return true; }
bool SANBA_BEHAVIORAL_SDK_GEDRAGS::Gebruikerprofiel() { return true; }
