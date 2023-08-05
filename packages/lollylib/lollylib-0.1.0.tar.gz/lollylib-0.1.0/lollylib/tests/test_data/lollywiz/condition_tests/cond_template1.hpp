[## if SHOW_FULL_COMMENT ##]
/**
* @author: [$$AUTHOR$$] 
* @date: [$$CURRENT_DATE$$]
* @brief: TODO: add your description
*/
[## elif SHOW_BRIEF_COMMENT ##]
/**
* @brief: TODO: add your description
*/
[## endif ##]
class [$$CLASS_NAME$$] {
[## if COND1 ##]
output1
[## elif COND_ALT1 ##]
output_alt1
[## elif COND_ALT2 ##]
output_alt2
[## else ##]
output_else
[## endif ##]
[##if COND1##]
output1 second time
[##else##]
output_else second time
[##endif##]
public:
    /// Interface
    /// Constructors
    [$$CLASS_NAME$$]() { }
    ~[$$CLASS_NAME$$]() { }
private:
    /// Here goes private part
};
