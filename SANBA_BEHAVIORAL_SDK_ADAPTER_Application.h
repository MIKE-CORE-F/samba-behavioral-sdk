#ifndef SANBA_BEHAVIORAL_SDK_ADAPTER_APPLICATION_H
#define SANBA_BEHAVIORAL_SDK_ADAPTER_APPLICATION_H

class SANBA_BEHAVIORAL_SDK_ADAPTER_Application {
public:
    SANBA_BEHAVIORAL_SDK_ADAPTER_Application();
    ~SANBA_BEHAVIORAL_SDK_ADAPTER_Application();

    bool Initialize(const char* appId);
    bool GetAppData(const char* key, char* value);
    bool SetAppData(const char* key, const char* value);

private:
    void* appId_;
};

#endif
