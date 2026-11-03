#ifndef SANBA_BEHAVIORAL_SDK_GEDRAGS_H
#define SANBA_BEHAVIORAL_SDK_GEDRAGS_H

class SANBA_BEHAVIORAL_SDK_GEDRAGS {
public:
    SANBA_BEHAVIORAL_SDK_GEDRAGS();
    ~SANBA_BEHAVIORAL_SDK_GEDRAGS();

    bool Initialize();
    bool Licentiecontrole();
    bool Gebruikerauthenticatie();
    bool Gebruikerprofiel();

private:
    void* gedragsdata_;
};

#endif
