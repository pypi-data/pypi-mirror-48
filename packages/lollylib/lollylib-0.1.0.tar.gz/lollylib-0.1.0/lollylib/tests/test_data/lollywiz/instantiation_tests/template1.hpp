[## if SHOW_FULL_COMMENT ##]
/**
* @author: [$$AUTHOR$$] 
* @date: [$$__DATE__$$]
* @brief: TODO: add your description
*/
[## elif SHOW_BRIEF_COMMENT ##]
/**
* @brief: TODO: add your description
*/
[## endif ##]
class [$$CLASS_NAME$$] {
[## if COND1 ##]
/// This is template1 with condition1
[## else ##]
/// This is default template1
[## endif ##]
public:
    /// Interface
    /// Constructors
    [$$CLASS_NAME$$]() { }
    ~[$$CLASS_NAME$$]() { }
private:
    /// Here goes private part
};
