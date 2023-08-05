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
/// This is template0 with condition1
[## else ##]
/// This is default template0
[## endif ##]
public:
    /// Interface
    /// Constructors
    [$$CLASS_NAME$$]() { }
    ~[$$CLASS_NAME$$]() { }
private:
    /// Here goes private part
};
